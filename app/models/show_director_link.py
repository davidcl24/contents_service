from sqlmodel import SQLModel, Field


class ShowDirectorLink(SQLModel, table=True):
    __tablename__ = "shows_directors"

    show_id: int | None = Field(default=None, foreign_key="shows.id", primary_key=True)
    director_id: int | None = Field(default=None, foreign_key="directors.id", primary_key=True)