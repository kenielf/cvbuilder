from os import getenv

from pydantic import BaseModel


class Base(BaseModel):
    model_config = {} if getenv("LOOSE_SCHEMA", "") == "1" else {"extra": "forbid"}
