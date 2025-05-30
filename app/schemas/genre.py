from sqlmodel import SQLModel


class GenreCreate(SQLModel):
    name: str

class GenreResponse(GenreCreate):
    id: int

class GenreUpdate(SQLModel):
    name: str | None