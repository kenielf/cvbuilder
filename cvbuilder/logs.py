from sys import stderr


def debug(msg: str):
    print(f"\x1b[36m[DEBUG]\x1b[00m {msg}", file=stderr)


def info(msg: str):
    print(f"\x1b[34m[INFO]\x1b[00m {msg}", file=stderr)


def error(msg: str):
    print(f"\x1b[31m[ERROR]\x1b[00m {msg}", file=stderr)
