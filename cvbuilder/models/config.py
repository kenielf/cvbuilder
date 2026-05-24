from cvbuilder.models import Base
from cvbuilder.models.identity import Identity
from cvbuilder.models.meta import Meta
from cvbuilder.models.profiles import Profile


class Config(Base):
    identity: Identity
    meta: Meta | None = None
    profile: list[Profile]

    # def __init__(self, data: dict):
    #     self.identity = Identity.model_validate(data["identity"])

    def toString(self):
        fields = [f"\t{name}\n" for name in Config.model_fields.items()]
        return f"Config(\n{', '.join(fields)})"

    # def __str__(self):
    #     return f"Config(Teste)"

    def get_override(self, key: str) -> str | None:
        if self.meta and self.meta.overrides:
            if self.meta.overrides.titles:
                return self.meta.overrides.titles.get(key, None)
