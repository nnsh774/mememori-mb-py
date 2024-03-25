__all__ = ('Enum',)

import enum
from typing import Any

class EnumMeta(enum.EnumMeta):
    default = str()

    def __call__(cls, _value: str= default, *args: Any, **kwargs: Any) -> Any:
        if _value is EnumMeta.default:
            return next(iter(cls))
        return super().__call__(_value, *args, **kwargs)

class Enum(enum.Enum, metaclass=EnumMeta):
    pass
