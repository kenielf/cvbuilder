from cvbuilder.models import Base


@Base.doc("Holds the information for language proficiencies, test proof codes are optional")
class Language(Base):
    name: str
    level: str
    test: str | None = None
    test_registration: str | None = None
    test_code: str | None = None
