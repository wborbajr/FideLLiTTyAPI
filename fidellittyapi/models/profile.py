from typing import Optional

from .rwmodel import RWModel

# from pydantic import UrlStr


class Profile(RWModel):
    username: str
    bio: Optional[str] = ""
    image: Optional[str] = None
    following: bool = False


class ProfileInResponse(RWModel):
    profile: Profile
