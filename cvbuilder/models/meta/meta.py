from cvbuilder.models import Base
from cvbuilder.models.meta.overrides import Overrides


class Meta(Base):
    overrides: Overrides | None = None
