from cvbuilder.models import Base
from cvbuilder.models.meta.overrides import Overrides


# TODO: Add the documentation decorator
class Meta(Base):
    overrides: Overrides | None = None
