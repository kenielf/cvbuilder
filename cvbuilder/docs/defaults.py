from dataclasses import dataclass
from typing import TypeVar

T = TypeVar("T")


DEFAULT_DOC_DICT = {
    "text": None,
    "note": None,
    "warn": None,
}


@dataclass(frozen=True)
class Documentation:
    text: str | None = None
    note: str | None = None
    warn: str | None = None


def doc(
    text: str,
    note: str | None = None,
    warn: str | None = None,
):
    def decorator(cls: T) -> T:
        cls.__documentation__ = Documentation(
            text=text,
            note=note,
            warn=warn,
        )
        return cls

    return decorator
