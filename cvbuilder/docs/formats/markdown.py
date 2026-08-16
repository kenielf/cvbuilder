from cvbuilder.docs.formatter import FormatterMap

FORMATTER: FormatterMap = {
    "class_": lambda cls: f"## {cls.__name__}",
    "anchor": lambda cls: f'<a id="{cls.__name__.lower()}"></a>',
    "section": lambda title: f"### {title}",
    "subsection": lambda title: f"#### {title}",
    "field": lambda name, type_str: f"- **{name}**: `{type_str}`",
    "field_meta": lambda text: f"  - {text}",
}
