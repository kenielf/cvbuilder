from cvbuilder.models import Base
from cvbuilder.models.profiles.education import Education
from cvbuilder.models.profiles.experience import Experience
from cvbuilder.models.profiles.language import Language
from cvbuilder.models.profiles.project import Project
from cvbuilder.models.profiles.skills import Skills


# TODO: Add the documentation decorator
class Profile(Base):
    name: str
    skills: list[Skills] | None = None
    language: list[Language] | None = None
    experience: list[Experience] | None = None
    project: list[Project] | None = None
    education: list[Education] | None = None

    def target_path(self):
        return f"cv-{self.name.lower().replace(" ", "_").replace("/", "-")}.tex"
