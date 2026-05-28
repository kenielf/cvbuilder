from pathlib import Path

from cvbuilder.args import PARSER
from cvbuilder.config import ConfigError, parse_config
from cvbuilder.logs import error, fatal, info
from cvbuilder.tex import CompilerCheckFailure, build, cleanup, tex_check


def main():
    args = PARSER.parse_args()

    try:
        tex_check()
    except CompilerCheckFailure as e:
        fatal(str(e))

    match args.command:
        case "build":
            failures = []
            for identity in args.paths:
                p = Path(identity)
                try:
                    config = parse_config(p)

                    for profile in config.profile:
                        info(f"Compiling Profile: {profile.name}")
                        build(config, profile)
                except ConfigError as e:
                    error(f"{type(e).__name__}: {str(e)}")
                    failures.append(p.name)
                    continue

            if failures:
                fatal("One or more compilations failed", code=2)

        case "clean":
            info(f"Cleaning up all profiles...")
            cleanup(all=args.all)
