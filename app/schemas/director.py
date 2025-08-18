from sqlmodel import SQLModel
from datetime import date


class DirectorCreate(SQLModel):
    name: str
    birth: date | None = None

class DirectorResponse(DirectorCreate):
    id: int

class DirectorUpdate(SQLModel):
    name: str | None = None
    birth: date | None = None