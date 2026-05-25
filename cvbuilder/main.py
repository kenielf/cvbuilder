from pathlib import Path

from cvbuilder.args import PARSER
from cvbuilder.config import ConfigError, parse_config
from cvbuilder.logs import fatal, info
from cvbuilder.tex import CompilerCheckFailure, build, cleanup, tex_check


def main():
    args = PARSER.parse_args()

    try:
        tex_check()
        config = parse_config(Path(args.identity_file))

        for profile in config.profile:
            info(f"Compiling Profile: {profile.name}")
            build(config, profile)

        if args.cleanup:
            info(f"Cleaning up all profiles...")
            cleanup()
    except (CompilerCheckFailure, ConfigError) as e:
        fatal(f"{type(e).__name__}: {str(e)}")
