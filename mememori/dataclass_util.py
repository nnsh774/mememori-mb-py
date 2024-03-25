__all__ = ('expand_dataclass', 'expand_fparams')

import dataclasses
import datetime
import enum
import inspect
import sys

from types import GenericAlias, UnionType
from typing import Any, Callable, _GenericAlias # type: ignore

from .array_packed import ArrayPacked
from .flags import Flags

# inspect.get_annotations(.., eval_str=True) doesn't work because 
# field member types may not be exported.
def get_annotations(cls: type[Any]) -> dict[str, type[Any]]:
    fields = inspect.get_annotations(cls, eval_str=False)
    obj_globals = {}
    module_name = getattr(cls, '__module__', None)
    if module_name:
        module = sys.modules.get(module_name, None)
        if module:
            obj_globals = {**getattr(module, '__dict__', None)}
    unwrap = cls
    while hasattr(unwrap, '__wrapped__'):
        unwrap = unwrap.__wrapped__
    if hasattr(unwrap, '__globals__'):
        obj_globals = {**unwrap.__globals__}
    obj_globals['ArrayPacked'] = ArrayPacked
    obj_globals['Flags'] = Flags
    return {
        field: 
            eval(typ[1:] if typ[0] == '_' else typ, obj_globals, None)
            if isinstance(typ, str) else typ
        for field, typ in fields.items()
    }

def __expand_field(value: Any, type_: type) -> Any:
    if isinstance(type_, GenericAlias) or isinstance(type_, _GenericAlias):
        if type_.__origin__ is list:
            inner_type = type_.__args__[0]
            return [
                __expand_field(inner_value, inner_type)
                for inner_value in (value or [])
            ]
        elif type_.__origin__ is dict:
            inner_type1 = type_.__args__[0]
            inner_type2 = type_.__args__[1]
            return {
                __expand_field(key, inner_type1): __expand_field(inner_value, inner_type2)
                for key, inner_value in (value or {}).items()
            }
        elif type_.__origin__ is set:
            inner_type = type_.__args__[0]
            return {
                __expand_field(inner_value, inner_type)
                for inner_value in (value or [])
            }
        elif type_.__origin__ is Flags:
            return __expand_enum_flags(value, type_)
        else:
            raise TypeError(f'Unhandled type: {type_}')
    if isinstance(type_, UnionType):
        if len(type_.__args__) != 2 or type_.__args__[1] is not type(None):
            raise TypeError(f'Unhandled type: {type_}')
        type_ = type_.__args__[0]
    return __expand_obj(value, type_)

def __expand_cls(obj: dict[str, Any], cls: type) -> Any:
    params: dict[str, Any] = {}
    fields = {}
    for c in cls.mro():
        fields.update(get_annotations(c))
    for name, type_ in fields.items(): # type: ignore
        if name not in obj:
            params[name] = None
            continue
        params[name] = __expand_field(obj[name], type_)
    return cls(**params)

def __expand_array_packed(obj: list[Any], cls: type) -> Any:
    params: dict[str, Any] = {}
    fields = {}
    for c in cls.mro():
        fields.update(get_annotations(c))
    for (name, type_), value in zip(fields.items(), obj): # type: ignore
        params[name] = __expand_field(value, type_)
    return cls(**params)

def __expand_enum(obj: int, enum: type) -> Any:
    return enum(obj)

def __expand_enum_flags(obj: int, flags: _GenericAlias) -> Flags[Any]:
    inner_type = flags.__args__[0]
    return Flags([
        m for m in inner_type.__members__.values() # type: ignore
        if obj & m.value
    ])

def __expand_obj(obj: Any, cls_or_enum: type) -> Any:
    if obj is None:
        return None
    if cls_or_enum in (int, float, bool, str):
        return cls_or_enum(obj)
    if cls_or_enum is datetime.datetime:
        assert isinstance(obj, datetime.datetime), obj
        return obj
    if cls_or_enum is datetime.timedelta:
        assert isinstance(obj, int), obj
        if obj == 9223372036854775807:
            return datetime.timedelta.max
        elif obj == -9223372036854775808:
            return datetime.timedelta.min
        return datetime.timedelta(seconds=obj)
    if issubclass(cls_or_enum, ArrayPacked):
        assert isinstance(obj, list), obj
        return __expand_array_packed(obj, cls_or_enum)
    if hasattr(cls_or_enum, '__dataclass_fields__'):
        if isinstance(obj, list):
            obj = obj[-1]
        assert isinstance(obj, dict), obj
        return __expand_cls(obj, cls_or_enum)
    elif isinstance(cls_or_enum, _GenericAlias) and cls_or_enum.__origin__ is Flags:
        assert isinstance(obj, int), obj
        return __expand_enum_flags(obj, cls_or_enum)
    else:
        assert isinstance(obj, int), obj
        return __expand_enum(obj, cls_or_enum)

def expand_dataclass(type_: type | None, obj: Any) -> Any:
    if type_ is None:
        return None
    return __expand_obj(obj, type_)

def expand_fparams(func: Callable[..., Any], **kwargs: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for name, type_ in get_annotations(func).items():
        if name == 'return' or name == 'self':
            continue
        if name not in kwargs:
            out[name] = None
        else:
            out[name] = __expand_field(kwargs[name], type_)
    return out

def expand_enums_in_dict(pairs: list[tuple[Any, Any]]) -> dict[Any, Any]:
    return {key: value.value if isinstance(value, enum.Enum) else value for key, value in pairs}

def collapse_dataclass(value: Any) -> Any:
    if hasattr(type(value), '__dataclass_fields__'):
        if issubclass(type(value), ArrayPacked):
            return [collapse_dataclass(getattr(value, v)) for v in value.__dataclass_fields__.keys()]
        return dataclasses.asdict(value, dict_factory=expand_enums_in_dict)
    elif isinstance(value, list):
        return [collapse_dataclass(f) for f in value]
    elif isinstance(value, set):
        return {collapse_dataclass(f) for f in value}
    elif isinstance(value, dict):
        return {collapse_dataclass(k): collapse_dataclass(v) for k, v in value.items()}
    elif isinstance(value, enum.Enum):
        return value.value
    elif isinstance(value, datetime.datetime):
        return value.isoformat().replace('T', ' ')
    elif isinstance(value, datetime.timedelta):
        return value.total_seconds()
    else:
        return value
