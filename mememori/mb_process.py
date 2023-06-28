from enum import Enum
import json

from .flags import Flags
from . import types
from . import mb

def get_type(name):
    if name.endswith(' | None'):
        name = name[:-7]
    if name == 'int':
        return int
    if name == 'str':
        return str
    if name == 'float':
        return float
    if name == 'bool':
        return bool
    if hasattr(types, name):
        return getattr(types, name)
    return getattr(mb, name)

def expand_cls(obj, cls):
    params = {}
    for field in cls.__dataclass_fields__.values():
        if field.type.startswith('list['):
            inner_type = get_type(field.type[5:-1])
            params[field.name] = [expand_obj(value, inner_type) for value in obj[field.name] or []]
        elif field.type.startswith('Flags['):
            inner_type = get_type(field.type[6:-1])
            params[field.name] = Flags([
                m for m in inner_type.__members__.values()
                if obj[field.name] & m.value
            ])
        elif field.name in obj:
            params[field.name] = expand_obj(obj[field.name], get_type(field.type))
        else:
            params[field.name] = None
    return cls(**params)

def expand_enum(obj, enum):
    return enum(obj)

def expand_obj(obj, cls_or_enum):
    if obj == None:
        return None
    if cls_or_enum is int or cls_or_enum is float or cls_or_enum is bool or cls_or_enum is str:
        return cls_or_enum(obj)
    if hasattr(cls_or_enum, '__dataclass_fields__'):
        return expand_cls(obj, cls_or_enum)
    else:
        return expand_enum(obj, cls_or_enum)

def process_mb(objs, which):
    cls = get_type(which)
    return [expand_obj(obj, cls) for obj in objs]

class EnumJSONEncoder(json.JSONEncoder):
    def encode_enum(self, obj):
        name = obj.name if obj.name != 'None_' else 'None'
        return f'{obj.__class__.__name__}.{name}'

    def default(self, obj):
        if isinstance(obj, Enum):
            return self.encode_enum(obj)
        if isinstance(obj, Flags):
            return ' | '.join(self.encode_enum(e) for e in obj.values)
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    import sys
    import pprint

    from dataclasses import asdict

    with open(sys.argv[1], 'rt') as f:
        objs = json.load(f)
    out = process_mb(objs, sys.argv[2])
    print(json.dumps([asdict(obj) for obj in out], cls=EnumJSONEncoder, ensure_ascii=False, indent=2))

