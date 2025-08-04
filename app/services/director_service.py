from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.director import Director
from app.models.movie import Movie
from app.models.show import Show
from app.schemas.director import DirectorResponse, DirectorCreate, DirectorUpdate


class DirectorService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, director_data: DirectorCreate) -> DirectorResponse:
        director = Director(**director_data.model_dump())
        self.session.add(director)
        self.session.commit()
        self.session.refresh(director)
        return DirectorResponse(**director.model_dump())

    def get_all(self):
        query = select(Director)
        return self.session.exec(query).all()

    def get_by_id(self, director_id: int):
        return self.session.get(Director, director_id)

    def get_from_movie(self, movie_id: int):
        movie = self.session.get(Movie, movie_id)
        return movie.directors

    def get_from_show(self, show_id: int):
        show = self.session.get(Show, show_id)
        return show.directors

    def update(self, director_id: int, director_data: DirectorUpdate) -> Director:
        director = self.session.get(Director, director_id)
        if not director:
            raise HTTPException(status_code=404, detail="Director not found")

        director_dict = director_data.model_dump(exclude_unset=True)
        for key, value in director_dict.items():
            setattr(director, key, value)

        self.session.add(director)
        self.session.commit()
        self.session.refresh(director)
        return director

    def delete(self, director_id: int):
        director = self.session.get(Director, director_id)
        if not director:
            raise HTTPException(status_code=404, detail="Director not found")

        self.session.delete(director)
        self.session.commit()
        return {"message": "Director successfully deleted"}