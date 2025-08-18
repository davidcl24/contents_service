from sqlmodel import SQLModel, Field


class ShowActorLink(SQLModel, table=True):
    __tablename__ = "shows_actors"

    shows_id: int | None = Field(default=None, foreign_key="shows.id", primary_key=True)
    actors_id: int | None = Field(default=None, foreign_key="actors.id", primary_key=True)