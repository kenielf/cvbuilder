from cvbuilder.models import Base, Field


@Base.doc("A project entry, currently aimed at software; the language is optional")
class Project(Base):
    name: str = Field(description="Name of the project")
    language: str | None = Field(None, description="Main programming language used")
    details: list[str] = Field(description="Project highlights, one per item")
