from cvbuilder.models import Base


# TODO: Add the documentation decorator
class Identity(Base):
    first_name: str
    family_name: str

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
        return " ".join((self.first_name, self.family_name))
