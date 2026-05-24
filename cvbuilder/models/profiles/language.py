from cvbuilder.models import Base


class Language(Base):
    name: str
    level: str
    test: str | None = None
    test_registration: str | None = None
    test_code: str | None = None
