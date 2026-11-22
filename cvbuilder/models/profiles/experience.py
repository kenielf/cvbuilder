from cvbuilder.models import Base, Field


@Base.doc(
    "A professional experience entry; the location, end date and actions are optional"
)
class Experience(Base):
    at: str = Field(description="Company or contractor the work was done for")
    role: str = Field(description="Position held")
    location: str | None = Field(None, description="Where the work took place")
    start: str = Field(description="When the position started")
    end: str | None = Field(
        None, description="When the position ended; omit if it is ongoing"
    )
    actions: list[str] | None = Field(
        None, description="Responsibilities and achievements, one per item"
    )
