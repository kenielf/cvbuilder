from cvbuilder.models import Base, Field
from cvbuilder.models.identity.contact import Contact


@Base.doc("Personal details that identify the CV owner")
class Identity(Base):
    first_name: str = Field(description="Given name(s) of the person")
    family_name: str = Field(
        description="Family name(s) of the person; all but the last are abbreviated when shortened"
    )
    contact: Contact | None = Field(
        None, description="Contact details shown below the CV title"
    )

    def get_full_name(self, shorten: bool = False):
        if shorten:
            split = self.family_name.split(" ")
            if len(split) > 1:
                return " ".join(
                    (
                        self.first_name,
                        " ".join(
                            [
                                f"{x[0]}."
                                for x in self.family_name.split(" ")[:-1]
                                if x[0].isupper()
                            ]
                        ),
                        self.family_name.split(" ")[-1],
                    )
                )
        return f"{self.first_name} {self.family_name}"
