from cvbuilder.models import Base, Field


@Base.doc(
    "Values that replace the template defaults",
    note="Supported title keys: skills, languages, experience, projects, education",
)
class Overrides(Base):
    titles: dict[str, str] | None = Field(
        None, description="Maps a section key to the title rendered in its place"
    )
