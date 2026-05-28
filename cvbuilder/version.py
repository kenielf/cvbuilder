from importlib import metadata
from pathlib import Path
from tomllib import TOMLDecodeError, load

from cvbuilder.constants import PROJECT
from cvbuilder.logs import error

version: str
try:
    version = metadata.version(PROJECT)
except metadata.PackageNotFoundError:
    pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
    with open(pyproject_path, "rb") as pyproject:
        try:
            version = load(pyproject)["project"]["version"]
        except TOMLDecodeError:
            error(f"Failed to parse '{pyproject_path.name}' to get name.")
