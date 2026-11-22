from cvbuilder.models import Base, Field
from cvbuilder.models.meta.overrides import Overrides


@Base.doc("Settings that customize how the CV is rendered")
class Meta(Base):
    overrides: Overrides | None = Field(
        None, description="Optional overrides applied to template values"
    )
