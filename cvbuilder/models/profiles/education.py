from cvbuilder.models import Base, Field


@Base.doc("A school or university course, from primary to higher education")
class Education(Base):
    institution: str = Field(description="Name of the school or university")
    location: str = Field(description="Where the institution is located")
    level: str = Field(description="Degree or education level (e.g. Bachelor's)")
    course: str = Field(description="Name of the course or program")
    start: str = Field(description="When the course started")
    end: str = Field(description="When the course ended or is expected to end")
