from sqlmodel import SQLModel, Field


class ShowActorLink(SQLModel, table=True):
    __tablename__ = "shows_actors"

    show_id: int | None = Field(default=None, foreign_key="shows.id", primary_key=True)
    actor_id: int | None = Field(default=None, foreign_key="actors.id", primary_key=True)