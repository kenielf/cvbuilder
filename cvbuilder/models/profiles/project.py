from cvbuilder.models import Base


class Project(Base):
    name: str
    language: str | None = None
    details: list[str]
