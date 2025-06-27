from fastapi import APIRouter, Depends

from app.schemas.movie import MovieResponse, MovieCreate, MovieUpdate
from app.services.movie_service import MovieService

router = APIRouter(tags=["Movies"])

@router.post("/movies", response_model=MovieResponse)
async def create_movie(movie: MovieCreate, service: MovieService = Depends()):
    return service.create(movie)

@router.get("/movies", response_model=list[MovieResponse])
async def read_movies(service: MovieService = Depends()):
    return service.get_all()

@router.get("/movies/{movie_id}", response_model=MovieResponse)
async def read_movie(movie_id: int, service: MovieService = Depends()):
    return service.get_by_id(movie_id)

@router.get("/genres/{genre_id}/movies", response_model=list[MovieResponse])
async def read_movies_by_genre(genre_id: int, service: MovieService = Depends()):
    return service.get_by_genre(genre_id)

@router.get("/actors/{actor_id}/movies", response_model=list[MovieResponse])
async def read_movies_with_actor(actor_id: int, service: MovieService = Depends()):
    return service.get_with_actor(actor_id)

@router.get("/directors/{director_id}/movies", response_model=list[MovieResponse])
async def read_movies_with_director(director_id: int, service: MovieService = Depends()):
    return service.get_with_director(director_id)

@router.post("/movies/batch", response_model=list[MovieResponse])
async def read_movies_batch(ids: list[int], service: MovieService = Depends()):
    return service.get_batch(ids)

@router.patch("/movies/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: int, movie_data: MovieUpdate, service: MovieService = Depends()):
    return service.update(movie_id, movie_data)

@router.delete("/movies/{movie_id}", response_model=dict)
async def delete_movie(movie_id: int, service: MovieService = Depends()):
    return service.delete(movie_id)