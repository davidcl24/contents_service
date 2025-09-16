from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.actor import Actor
from app.models.director import Director
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieResponse, MovieUpdate


class MovieService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, movie_data: MovieCreate) -> MovieResponse:
        movie = Movie(**movie_data.model_dump())

        if movie_data.directors_ids:
            statement = select(Director).where(Director.id.in_(movie_data.directors_ids))
            directors = list(self.session.exec(statement).all())
            movie.directors = directors

        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return MovieResponse(**movie.model_dump())

    def get_all(self):
        query = select(Movie)
        return self.session.exec(query).all()

    def get_by_id(self, movie_id: int):
        return self.session.get(Movie, movie_id)

    def get_by_genre(self, genre_id: int):
        statement = select(Movie).where(Movie.genre_id == genre_id)
        result = self.session.exec(statement)
        return result.all()

    def get_with_actor(self, actor_id: int):
        actor = self.session.get(Actor, actor_id)
        return actor.movies

    def get_with_director(self, director_id: int):
        director = self.session.get(Director, director_id)
        return director.movies

    def get_batch(self, ids: list[int]):
        statement = select(Movie).where(Movie.id.in_(ids))
        results = self.session.exec(statement).all()

        if not results:
            raise HTTPException(status_code=404, detail="Movies not found")

        return results

    def update(self, movie_id: int, movie_data: MovieUpdate) -> Movie:
        movie = self.session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        movie_dict = movie_data.model_dump(exclude_unset=True, exclude={"directors_ids"})
        for key, value in movie_dict.items():
            setattr(movie, key, value)

        if movie_data.directors_ids:
            statement = select(Director).where(Director.id.in_(movie_data.directors_ids))
            directors = list(self.session.exec(statement).all())
            movie.directors = directors

        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return movie

    def delete(self, movie_id: int):
        movie = self.session.get(Movie, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")

        self.session.delete(movie)
        self.session.commit()
        return {"message": "Movie successfully deleted"}
