from argparse import ArgumentParser

from cvbuilder.constants import PROJECT, PROJECT_DESCRIPTION
from cvbuilder.version import version
from pathlib import Path

PARSER = ArgumentParser(prog=PROJECT, epilog=f"{PROJECT_DESCRIPTION} v{version}")

subparsers = PARSER.add_subparsers(
    dest="command",
    required=True,
)

# Build
build = subparsers.add_parser(
    "build",
    help="Build identities from one or more paths",
)

build.add_argument(
    "paths",
    type=Path,
    nargs="+",
    help="One or more identity paths",
)

# Clean
clean = subparsers.add_parser(
    "clean",
    help="Remove generated artifacts",
)

clean.add_argument(
    "-A",
    "--all",
    action="store_true",
    help="Remove all artifacts, including caches and intermediates",
)
