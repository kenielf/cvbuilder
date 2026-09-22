from cvbuilder.models import Base


@Base.doc("Holds the information for listing the skills in a list format, scoped")
class Skills(Base):
    scope: str
    values: list[str]
