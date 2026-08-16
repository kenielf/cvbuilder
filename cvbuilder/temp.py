from typing import Union, get_args, get_origin

from pydantic import BaseModel


def fmt_type(tp):
    origin = get_origin(tp)
    args = get_args(tp)

    if origin is None:
        return tp.__name__ if hasattr(tp, "__name__") else str(tp)

    if origin is Union:
        return f"Union[{', '.join(fmt_type(a) for a in args)}]"

    return f"{origin.__name__}[{', '.join(fmt_type(a) for a in args)}]"


def find_model(tp):
    if isinstance(tp, type) and issubclass(tp, BaseModel):
        return tp

    origin = get_origin(tp)
    if not origin:
        return None

    for arg in get_args(tp):
        m = find_model(arg)
        if m:
            return m
    return None


def print_model_types(model: type[BaseModel], indent=0):
    pad = " " * indent
    suffix = " (Model)" if issubclass(model, BaseModel) else ""
    print(f"{pad}{model.__name__}{suffix}")

    for name, field in model.model_fields.items():
        ann = field.annotation
        print(f"{pad}  {name}:")

        nested = find_model(ann)
        if nested:
            print_model_types(nested, indent + 4)
        else:
            print(f"{pad}    {fmt_type(ann)}")
