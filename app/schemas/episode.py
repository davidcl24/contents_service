"""
Episode schemas that map the JSON that comes from the request
or has to be sent back as a reply
"""
from datetime import date

from sqlmodel import SQLModel


class EpisodeCreate(SQLModel):
    """Schema that contains the necessary data to create a new episode"""
    title: str
    synopsis: str | None = None
    season_num: int | None = None
    episode_num: int | None = None
    length: int | None = None
    release_date: date | None = None
    show_id: int | None = None
    file_key: str | None = None  # Delete the None in production

class EpisodeResponse(EpisodeCreate):
    """Schema that contains the episode data that should be returned to the client. It inherits the create schema"""
    id: int

class EpisodeUpdate(SQLModel):
    """Schema used to update an existing episode"""
    title: str | None = None
    synopsis: str | None = None
    season_num: int | None = None
    episode_num: int | None = None
    length: int | None = None
    release_date: date | None = None
    show_id: int | None = None
    file_key: str | None = None  # Delete the None in production