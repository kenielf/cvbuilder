from argparse import ArgumentParser
from pathlib import Path

from cvbuilder.constants import PROJECT, PROJECT_DESCRIPTION
from cvbuilder.version import version

PARSER = ArgumentParser(prog=PROJECT, epilog=f"{PROJECT_DESCRIPTION} v{version}")

subparsers = PARSER.add_subparsers(
    dest="command",
    required=True,
)

# Docs
docs = subparsers.add_parser("docs", help="Show the schema documentation")

fmt = docs.add_mutually_exclusive_group()

fmt.add_argument(
    "--markdown",
    dest="format",
    action="store_const",
    const="markdown",
    help="Render documentation as Markdown",
)

fmt.add_argument(
    "--plain",
    dest="format",
    action="store_const",
    const="plain",
    help="Render documentation as Plaintext",
)

docs.set_defaults(format="plain")

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
