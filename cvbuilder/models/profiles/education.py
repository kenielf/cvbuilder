from cvbuilder.models import Base


class Education(Base):
    institution: str
    location: str
    level: str
    course: str
    start: str
    end: str
