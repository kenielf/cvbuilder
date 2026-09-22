from cvbuilder.models import Base
from cvbuilder.models.meta.overrides import Overrides


@Base.doc("This is the overrides model - used for replacing values in templates")
class Meta(Base):
    overrides: Overrides | None = None
