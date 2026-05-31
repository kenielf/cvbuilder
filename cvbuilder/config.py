from pathlib import Path
from tomllib import TOMLDecodeError, load

from pydantic import ValidationError
from pydantic_core import ErrorDetails

from cvbuilder.logs import debug
from cvbuilder.models.config import Config


class ConfigError(Exception):
    pass


def parse_model_error(e: ErrorDetails):
    *parents, child = map(str, e["loc"])
    parent = ".".join(parents)
    full = child if not parent else f"{parent}.{child}"
    entry = e["input"]

    message = ""
    match e["type"]:
        case "missing":
            message = f"Missing mandatory '{child}' at {parent}: {entry}"
        case "extra_forbidden":
            message = f"Forbidden '{child}' with value '{entry}' at {parent}"
        case t if str(t).endswith("_type") or str(t).endswith("_parsing"):
            expected = t.split("_")[0]
            received = type(entry).__name__
            message = (
                f"Expected {expected} at {full}, got '{received}' ({entry}) instead"
            )
        case _:
            debug(f"Unknown error: {e["type"]}")
            message = "Unknown"

    return message


def parse_config(f: Path) -> Config:
    if not f.exists():
        raise ConfigError(f"Cannot parse configuration: file '{f.name}' does not exist")

    with open(f, "rb") as file:
        try:
            data = load(file)
        except TOMLDecodeError as e:
            raise ConfigError(
                f"Cannot parse configuration: file '{f.name}' is malformed "
                f"(L#{e.lineno}, C#{e.colno})"
            ) from e

    try:
        return Config.model_validate(data)
    except ValidationError as errors:
        # TODO: Maybe move exceptions into a base exception class for better formatting
        reasons = [parse_model_error(e) for e in errors.errors()]
        if len(reasons) > 1:
            raise ConfigError(f"Found multiple configuration errors:\n\t- " + "\n\t- ".join(reasons))
        else:
            raise ConfigError(f"Found a cofiguration error: {reasons[0]}")
