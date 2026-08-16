from os import getenv

from pydantic import BaseModel, Field

from cvbuilder.docs.defaults import DEFAULT_DOC_DICT, doc


class Base(BaseModel):
    __documentation__ = DEFAULT_DOC_DICT.copy()
    doc = staticmethod(doc)

    model_config = (
        {}
        if getenv("LOOSE_SCHEMA", "") == "1"
        else {"extra": "forbid"}
    )
