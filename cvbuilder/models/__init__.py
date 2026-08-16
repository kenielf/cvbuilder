from os import getenv

from pydantic import BaseModel, Field

from cvbuilder.docs.defaults import DEFAULT_DOC_DICT


class Base(BaseModel):
    __documentation__ = DEFAULT_DOC_DICT.copy()
    model_config = {} if getenv("LOOSE_SCHEMA", "") == "1" else {"extra": "forbid"}

    @staticmethod
    def doc(text: str, note: str | None = None, warn: str | None = None):
        def decorator(cls):
            cls.__documentation__ = {"text": text, "note": note, "warn": warn}
            return cls

        return decorator
