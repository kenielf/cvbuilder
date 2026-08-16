DEFAULT_DOC_DICT = {
    "text": None,
    "note": None,
    "warn": None,
}


def doc(
    text: str,
    note: str | None = None,
    warn: str | None = None,
):
    def decorator(cls):
        cls.__documentation__ = {
            "text": text,
            "note": note,
            "warn": warn,
        }
        return cls

    return decorator
