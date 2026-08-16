from typing import Literal, Union, get_args, get_origin

from pydantic import BaseModel


def is_pydantic_model(tp) -> bool:
    try:
        return issubclass(tp, BaseModel)
    except TypeError:
        return False


def anchor_for(cls: type[BaseModel]) -> str:
    return cls.__name__.lower()


def format_literal(tp) -> str:
    values = ", ".join(repr(v) for v in get_args(tp))
    return f"Literal[{values}]"


def format_type(tp) -> tuple[str, bool, list[type[BaseModel]]]:
    """
    Returns:
        type_str: human-readable type
        is_optional: whether Optional
        refs: referenced submodels
    """
    origin = get_origin(tp)
    refs: list[type[BaseModel]] = []

    # Optional / Union
    if origin is Union:
        args = get_args(tp)
        if type(None) in args:
            non_none = [a for a in args if a is not type(None)]
            type_str, _, sub = format_type(non_none[0])
            return type_str, True, sub

    # Literal
    if origin is Literal:
        return format_literal(tp), False, []

    # Containers
    if origin in (list, set, tuple):
        inner = get_args(tp)[0]
        inner_str, _, sub = format_type(inner)
        refs.extend(sub)
        return f"list[{inner_str}]", False, refs

    if origin is dict:
        _, value = get_args(tp)
        value_str, _, sub = format_type(value)
        refs.extend(sub)
        return f"dict[str, {value_str}]", False, refs

    # Nested Pydantic model
    if is_pydantic_model(tp):
        refs.append(tp)
        return tp.__name__, False, refs

    # Primitive / fallback
    return getattr(tp, "__name__", str(tp)), False, refs
