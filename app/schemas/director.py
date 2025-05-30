from sqlmodel import SQLModel


class DirectorCreate(SQLModel):
    name: str
    birth: str | None = None

class DirectorResponse(DirectorCreate):
    id: int

class DirectorUpdate(SQLModel):
    name: str | None = None
    birth: str | None = None