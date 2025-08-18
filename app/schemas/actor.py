from sqlmodel import SQLModel
from datetime import date


class ActorCreate(SQLModel):
    name: str
    birth: date | None = None

class ActorResponse(ActorCreate):
    id: int

class ActorUpdate(SQLModel):
    name: str | None = None
    birth: date | None = None