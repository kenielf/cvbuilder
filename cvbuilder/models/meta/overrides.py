from cvbuilder.models import Base


class Overrides(Base):
    titles: dict[str, str] | None = None
