from typing import Protocol, Type, TypedDict

from pydantic import BaseModel


class ClassFormatter(Protocol):
    def __call__(self, cls: Type[BaseModel]) -> str: ...


class AnchorFormatter(Protocol):
    def __call__(self, cls: Type[BaseModel]) -> str: ...


class SectionFormatter(Protocol):
    def __call__(self, title: str) -> str: ...


class SubsectionFormatter(Protocol):
    def __call__(self, title: str) -> str: ...


class FieldFormatter(Protocol):
    def __call__(self, name: str, type_str: str) -> str: ...


class FieldMetaFormatter(Protocol):
    def __call__(self, text: str) -> str: ...


class FormatterMap(TypedDict):
    class_: ClassFormatter
    anchor: AnchorFormatter
    section: SectionFormatter
    subsection: SubsectionFormatter
    field: FieldFormatter
    field_meta: FieldMetaFormatter
