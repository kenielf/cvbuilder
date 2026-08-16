from cvbuilder.docs.formatter import FormatterMap

RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
DIM = "\033[2m"

FORMATTER: FormatterMap = {
    "class_": lambda cls: f"{BOLD}{cls.__name__}{RESET}",
    "anchor": lambda cls: f"{DIM}#{cls.__name__.lower()}{RESET}",
    "section": lambda title: f"\n{BOLD}{title}{RESET}",
    "subsection": lambda title: f"{ITALIC}{title}{RESET}",
    "field": lambda name, type_str: (
        f"  {BOLD}{name}{RESET}: {ITALIC}{type_str}{RESET}"
    ),
    "field_meta": lambda text: f"    {DIM}{text}{RESET}",
}
