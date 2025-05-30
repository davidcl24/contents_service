from sqlmodel import SQLModel, Field


class ShowDirectorLink(SQLModel, table=True):
    __tablename__ = "shows_directors"

    show_id: int | None = Field(default=None, foreign_key="show.id", primary_key=True)
    director_id: int | None = Field(default=None, foreign_key="director.id", primary_key=True)