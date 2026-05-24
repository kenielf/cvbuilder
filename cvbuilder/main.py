from pathlib import Path

from cvbuilder.config import ConfigError, parse_config
from cvbuilder.logs import error, info
from cvbuilder.tex import CompilationFailure, CompilerCheckFailure, build, tex_check


def main():
    # TODO: Implement CLI interface
    f = "./identity.toml"
    try:
        config = parse_config(Path(f))
    except ConfigError as e:
        error(str(e))
        exit(1)

    try:
        tex_check()
    except CompilerCheckFailure as e:
        error(str(e))
        exit(1)

    for profile in config.profile:
        try:
            info(f"Compiling Profile: {profile.name}")
            build(config, profile)
        except CompilationFailure as e:
            error(str(e))
