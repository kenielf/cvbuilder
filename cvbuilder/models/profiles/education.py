from cvbuilder.models import Base


@Base.doc("Holds the info for the primary/higher education courses")
class Education(Base):
    institution: str
    location: str
    level: str
    course: str
    start: str
    end: str
