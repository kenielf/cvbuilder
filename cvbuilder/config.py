from pathlib import Path
from tomllib import load

from pydantic import ValidationError

from cvbuilder.models.config import Config


class ConfigError(Exception):
    pass


def parse_config(f: Path):
    if not f.exists():
        raise ConfigError(f"Cannot parse configuration: file '{f.name}' does not exist")

    with open(f, "rb") as file:
        data = load(file)

    try:
        config = Config.model_validate(data)
    except ValidationError as errors:
        for e in errors.errors():
            if e["type"] == "extra_forbidden":
                print(
                    ".".join((str(x) for x in e["loc"])),
                    "=",
                    e["input"],
                    "is not allowed",
                )
            else:
                print(e)
        exit(1)

    return config
