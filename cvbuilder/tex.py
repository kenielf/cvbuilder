from os import chdir, getcwd
from pathlib import Path
from subprocess import PIPE, CalledProcessError, run

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from cvbuilder.logs import debug, error
from cvbuilder.models.config import Config
from cvbuilder.models.profiles.profiles import Profile


BUILD_PATH = Path(__file__).parent.parent / ".build"
COMPILER_PROG = "lualatex"
COMPILER_ARGS = (
    "-interaction=nonstopmode",
    "-halt-on-error",
)

DEFAULT_TEMPLATE = "compact.tex.j2"

ENV = Environment(
    loader=FileSystemLoader("templates"), undefined=StrictUndefined, autoescape=False
)


class CompilationFailure(Exception):
    pass


def lualatex_check():
    # TODO: Implement
    pass


# FIXME: This is deadcode, not sure if escaping is better done on render or in input
def tex_escape(s: str):
    return s.replace(r"#", r"\#")


def compile(p: Path, name: str, is_rerun: bool = False):
    pwd = getcwd()
    try:
        chdir(BUILD_PATH)
        r = run(
            [COMPILER_PROG, *COMPILER_ARGS, str(p).split("/")[-1]],
            stdout=PIPE,
            stderr=PIPE,
            check=True,
            timeout=30,
            text=True,
        )
        if "Package rerunfilecheck Warning:" in r.stdout:
            if not is_rerun:
                debug("Compilation successful, but requires rerun")
                compile(p, name, is_rerun=True)
            else:
                error("Requested rerun on rerun, bad.")
        chdir(pwd)
    except CalledProcessError as e:
        if getcwd() == BUILD_PATH:
            chdir(pwd)
        raise CompilationFailure(
            f"Failed to compile the {name} profile - {COMPILER_PROG} returned {e.returncode}"
            # TODO: Implement parsing of the tex compilation
            # + e.stdout
            # ", ".join([line for line in e.stdout.split("\n") if line.startswith("!")])
        )


def build(c: Config, p: Profile):
    if not BUILD_PATH.exists():
        try:
            BUILD_PATH.mkdir()
        except PermissionError:
            raise CompilationFailure(
                f"Could not create build directory at '{BUILD_PATH}': permission error"
            )

    try:
        # TODO: Override this in the user data/configuration
        path = BUILD_PATH / p.target_path()
        with open(path, "w") as file:
            file.write(ENV.get_template(DEFAULT_TEMPLATE).render(config=c, profile=p))
        compile(path, p.name)
        # TODO: Cleanup
    except Exception as e:
        raise CompilationFailure(e)
