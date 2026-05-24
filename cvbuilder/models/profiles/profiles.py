from cvbuilder.models import Base
from cvbuilder.models.profiles.education import Education
from cvbuilder.models.profiles.experience import Experience
from cvbuilder.models.profiles.language import Language
from cvbuilder.models.profiles.project import Project
from cvbuilder.models.profiles.skills import Skills


class Profile(Base):
    name: str
    skills: list[Skills]
    language: list[Language]
    experience: list[Experience]
    project: list[Project]
    education: list[Education]

    def target_path(self):
        return f"cv-{self.name.lower().replace(" ", "_")}.tex"
