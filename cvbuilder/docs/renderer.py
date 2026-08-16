from pydantic import BaseModel
from pydantic_core import PydanticUndefined

from cvbuilder.docs.formats.markdown import FORMATTER as MD
from cvbuilder.docs.formats.plain import FORMATTER as PLAIN
from cvbuilder.docs.formatter import FormatterMap
from cvbuilder.docs.types import anchor_for, format_type
from cvbuilder.models.config import Config


def render(fmt: str) -> str:
    match fmt:
        case "markdown":
            return _render_model(Config, MD)
        case "plain":
            return _render_model(Config, PLAIN)
        case _:
            raise RuntimeError(f"Unknown format: {fmt}")


def _render_model(
    root: type[BaseModel],
    fmt: FormatterMap,
    seen: set[type[BaseModel]] | None = None,
) -> str:
    if seen is None:
        seen = set()

    if root in seen:
        return ""

    seen.add(root)

    lines: list[str] = []
    submodels: set[type[BaseModel]] = set()

    # Model header
    lines.append(fmt["class_"](root))
    lines.append(fmt["anchor"](root))

    # Class documentation
    doc = getattr(root, "__documentation__", None)
    if doc and doc.get("text"):
        lines.append(doc["text"])

    # Fields section
    lines.append(fmt["section"]("Fields"))

    for name, field in root.model_fields.items():
        type_str, optional, refs = format_type(field.annotation)

        if optional:
            type_str += " (Optional)"

        line = fmt["field"](name, type_str)

        for ref in refs:
            if ref is not root:
                line += f" (see {ref.__name__})"
                submodels.add(ref)

        lines.append(line)

        if field.description:
            lines.append(fmt["field_meta"](field.description))

        if field.default not in (None, PydanticUndefined):
            lines.append(fmt["field_meta"](f"Default: {field.default!r}"))

    # Nested models
    for sub in sorted(submodels, key=lambda c: c.__name__):
        lines.append("")
        lines.append(_render_model(sub, fmt, seen))

    return "\n".join(lines)
