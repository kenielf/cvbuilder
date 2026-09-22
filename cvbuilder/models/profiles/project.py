from cvbuilder.models import Base


@Base.doc("Holds the information for coding (for now) projects, languages are optional")
class Project(Base):
    name: str
    language: str | None = None
    details: list[str]
