from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.actor import Actor
from app.models.director import Director
from app.models.show import Show
from app.schemas.show import ShowCreate, ShowResponse, ShowUpdate


class ShowService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, show_data: ShowCreate) -> ShowResponse:
        show = Show(**show_data.model_dump())

        if show_data.directors_ids:
            statement = select(Director).where(Director.id.in_(show_data.directors_ids))
            directors = list(self.session.exec(statement).all())
            show.directors = directors

        if show_data.actors_ids:
            statement = select(Actor).where(Actor.id.in_(show_data.actors_ids))
            actors = list(self.session.exec(statement).all())
            show.actors = actors

        self.session.add(show)
        self.session.commit()
        self.session.refresh(show)
        return ShowResponse(**show.model_dump())

    def get_all(self):
        query = select(Show)
        return self.session.exec(query).all()

    def get_by_id(self, show_id: int):
        return self.session.get(Show, show_id)

    def get_by_genre(self, genre_id: int):
        statement = select(Show).where(Show.genre_id == genre_id)
        result = self.session.exec(statement)
        return result.all()

    def get_with_actor(self, actor_id):
        actor = self.session.get(Actor, actor_id)
        return actor.shows

    def get_with_director(self, director_id):
        director = self.session.get(Director, director_id)
        return director.shows

    def get_batch(self, ids: list[int]):
        statement = select(Show).where(Show.id.in_(ids))
        results = self.session.exec(statement).all()

        if not results:
            raise HTTPException(status_code=404, detail="Shows not found")

        return results

    def update(self, show_id: int, show_data: ShowUpdate) -> Show:
        show = self.session.get(Show, show_id)
        if not show:
            raise HTTPException(status_code=404, detail="Show not found")

        show_dict = show_data.model_dump(exclude_unset=True, exclude={"directors_ids", "actors_ids"})
        for key, value in show_dict.items():
            setattr(show, key, value)

        if show_data.directors_ids:
            statement = select(Director).where(Director.id.in_(show_data.directors_ids))
            directors = list(self.session.exec(statement).all())
            show.directors = directors

        if show_data.actors_ids:
            statement = select(Actor).where(Actor.id.in_(show_data.actors_ids))
            actors = list(self.session.exec(statement).all())
            show.actors = actors

        self.session.add(show)
        self.session.commit()
        self.session.refresh(show)
        return show

    def delete(self, show_id: int):
        show = self.session.get(Show, show_id)
        if not show:
            raise HTTPException(status_code=404, detail="Show not found")

        self.session.delete(show)
        self.session.commit()
        return {"message": "Show successfully deleted"}