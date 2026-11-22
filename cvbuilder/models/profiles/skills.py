from cvbuilder.models import Base, Field


@Base.doc("A list of skills grouped under a scope")
class Skills(Base):
    scope: str = Field(description="Category the skills belong to")
    values: list[str] = Field(description="Skills listed under this scope")
