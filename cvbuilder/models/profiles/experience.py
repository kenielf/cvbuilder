from cvbuilder.models import Base


@Base.doc("Holds the professional experience, end times and actions are optional")
class Experience(Base):
    at: str
    role: str
    location: str | None = None
    start: str
    end: str | None = None
    actions: list[str] | None = None
