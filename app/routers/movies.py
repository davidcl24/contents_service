"""
It contains all of the endpoints directly related to movies
"""

from fastapi import APIRouter, Depends

from app.schemas.movie import MovieResponse, MovieCreate, MovieUpdate, MovieResponseExtended
from app.services.movie_service import MovieService

router = APIRouter(tags=["Movies"])

@router.post("/movies", response_model=MovieResponse)
async def create_movie(movie: MovieCreate, service: MovieService = Depends()):
    """Handles the specific POST HTTP request to create a new movie and returns the created movie as JSON if successful"""
    return service.create(movie)

@router.get("/movies", response_model=list[MovieResponse])
async def read_movies(service: MovieService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all existing movies as JSON"""
    return service.get_all()

@router.get("/movies/extended", response_model=list[MovieResponseExtended])
async def read_movies_extended(service: MovieService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all existing movies as an extended JSON with more data"""
    return service.get_all()

@router.get("/movies/{movie_id}", response_model=MovieResponse)
async def read_movie(movie_id: int, service: MovieService = Depends()):
    """Handles the specific GET HTTP request and returns a specific movie as JSON"""
    return service.get_by_id(movie_id)

@router.get("/movies/{movie_id}/extended", response_model=MovieResponseExtended)
async def read_movie(movie_id: int, service: MovieService = Depends()):
    """Handles the specific GET HTTP request and returns a specific movie as an extended JSON with more data"""
    return service.get_by_id(movie_id)

@router.get("/genres/{genre_id}/movies", response_model=list[MovieResponse])
async def read_movies_by_genre(genre_id: int, service: MovieService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all movies with a specific genre as JSON"""
    return service.get_by_genre(genre_id)

@router.get("/actors/{actor_id}/movies", response_model=list[MovieResponse])
async def read_movies_with_actor(actor_id: int, service: MovieService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all movies with a specific actor as JSON"""
    return service.get_with_actor(actor_id)

@router.get("/directors/{director_id}/movies", response_model=list[MovieResponse])
async def read_movies_with_director(director_id: int, service: MovieService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all movies with a specific director as JSON"""
    return service.get_with_director(director_id)

@router.post("/movies/batch", response_model=list[MovieResponse])
async def read_movies_batch(ids: list[int], service: MovieService = Depends()):
    """Handles the specific POST HTTP request and returns a list of the movies by a list of IDs as JSON"""
    return service.get_batch(ids)

@router.patch("/movies/{movie_id}", response_model=MovieResponse)
async def update_movie(movie_id: int, movie_data: MovieUpdate, service: MovieService = Depends()):
    """Handles the specific PATCH HTTP request to update an existing movie and returns the updated movie as JSON if successful"""
    return service.update(movie_id, movie_data)

@router.delete("/movies/{movie_id}", response_model=dict)
async def delete_movie(movie_id: int, service: MovieService = Depends()):
    """Handles the specific DELETE HTTP request to delete an existing movie and returns a dict as JSON if successful"""
    return service.delete(movie_id)