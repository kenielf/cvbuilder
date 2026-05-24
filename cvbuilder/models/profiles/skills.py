from cvbuilder.models import Base


class Skills(Base):
    scope: str
    values: list[str]
