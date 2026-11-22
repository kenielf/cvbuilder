from cvbuilder.models import Base, Field


@Base.doc("A language proficiency; the test details are optional")
class Language(Base):
    name: str = Field(description="Name of the language")
    level: str = Field(description="Proficiency level (e.g. Fluent, Basic)")
    test: str | None = Field(
        None, description="Name of the proficiency test taken (e.g. TOEFL)"
    )
    test_registration: str | None = Field(
        None, description="Label shown before the test code (e.g. Registration)"
    )
    test_code: str | None = Field(None, description="Code that proves the test result")
