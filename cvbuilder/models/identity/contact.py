import re

from cvbuilder.models import Base, Field


def _handle(value: str, domain: str, prefix: str = "") -> str:
    """Reduce a profile URL or handle to the bare handle."""
    value = re.sub(r"^(https?://)?(www\.)?", "", value.strip()).rstrip("/")
    value = value.removeprefix(f"{domain}/").removeprefix(prefix)
    return value.lstrip("@")


@Base.doc("Ways to reach the CV owner; every field is optional")
class Contact(Base):
    email: str | None = Field(None, description="Email address")
    phone: str | None = Field(
        None,
        description="Phone number, written as it should appear (e.g. +55 12 91234-5678)",
    )
    location: str | None = Field(
        None, description="Where the person lives (e.g. São José dos Campos, SP)"
    )
    website: str | None = Field(None, description="Personal website or portfolio URL")
    github: str | None = Field(None, description="GitHub username or profile URL")
    linkedin: str | None = Field(None, description="LinkedIn handle or profile URL")

    def phone_uri(self) -> str:
        return "tel:" + re.sub(r"[^\d+]", "", self.phone or "")

    def website_url(self) -> str:
        site = (self.website or "").strip()
        return site if re.match(r"^https?://", site) else f"https://{site}"

    def website_label(self) -> str:
        site = (self.website or "").strip()
        return re.sub(r"^(https?://)?(www\.)?", "", site).rstrip("/")

    def github_handle(self) -> str:
        return _handle(self.github or "", "github.com")

    def linkedin_handle(self) -> str:
        return _handle(self.linkedin or "", "linkedin.com", "in/")
