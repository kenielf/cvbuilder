import re

from cvbuilder.models import Base, Field
from cvbuilder.models.profiles.education import Education
from cvbuilder.models.profiles.experience import Experience
from cvbuilder.models.profiles.language import Language
from cvbuilder.models.profiles.project import Project
from cvbuilder.models.profiles.skills import Skills


@Base.doc(
    "One version of the CV; an identity can have several, each with its own sections"
)
class Profile(Base):
    name: str = Field(
        description="Profile name; used to build the output file name unless slug is set"
    )
    slug: str | None = Field(
        None,
        description="Output file name stem (without the cv- prefix); "
        "must be unique across all built profiles",
    )
    skills: list[Skills] | None = Field(None, description="Scoped skill lists")
    language: list[Language] | None = Field(None, description="Language proficiencies")
    experience: list[Experience] | None = Field(
        None, description="Professional experience entries"
    )
    project: list[Project] | None = Field(None, description="Project entries")
    education: list[Education] | None = Field(None, description="Education entries")

    def target_path(self) -> str:
        stem = self.slug or self.name
        stem = re.sub(r"[^\w.-]+", "-", stem.lower()).strip("-.")
        return f"cv-{stem or 'profile'}.tex"
