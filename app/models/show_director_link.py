from sqlmodel import SQLModel, Field


class ShowDirectorLink(SQLModel, table=True):
    __tablename__ = "shows_directors"

    shows_id: int | None = Field(default=None, foreign_key="shows.id", primary_key=True)
    directors_id: int | None = Field(default=None, foreign_key="directors.id", primary_key=True)