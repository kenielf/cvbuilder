from argparse import ArgumentParser

from cvbuilder.constants import PROJECT, PROJECT_DESCRIPTION
from cvbuilder.version import version

PARSER = ArgumentParser(prog=PROJECT, epilog=f"{PROJECT_DESCRIPTION} v{version}")

# TODO: Should be able to (build, build && clean) or (clean)
PARSER.add_argument(
    "-i",
    "--identity-file",
    dest="identity_file",
    action="append",
    required=True,
    help="Path to the identity file",
)
PARSER.add_argument(
    "-c", "--cleanup", action="store_true", help="Enable cleanup after execution"
)
