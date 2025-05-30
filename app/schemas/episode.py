from datetime import date

from sqlmodel import SQLModel


class EpisodeCreate(SQLModel):
    title: str
    synopsis: str | None = None
    season_num: int | None = None
    episode_num: int | None = None
    length: int | None = None
    release_date: date | None = None
    show_id: int | None = None

class EpisodeResponse(EpisodeCreate):
    id: int

class EpisodeUpdate(SQLModel):
    title: str | None = None
    synopsis: str | None = None
    season_num: int | None = None
    episode_num: int | None = None
    length: int | None = None
    release_date: date | None = None
    show_id: int | None = None