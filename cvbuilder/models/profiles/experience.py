from cvbuilder.models import Base


class Experience(Base):
    at: str
    role: str
    location: str | None = None
    start: str
    end: str | None = None
    actions: list[str] | None = None
