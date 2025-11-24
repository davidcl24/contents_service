"""
It contains all of the endpoints directly related to shows
"""

from fastapi import APIRouter
from fastapi.params import Depends

from app.schemas.show import ShowResponse, ShowCreate, ShowUpdate, ShowResponseExtended
from app.services.show_service import ShowService

router = APIRouter(tags=["Shows"])

@router.post("/shows", response_model=ShowResponse)
async def create_show(show: ShowCreate, service: ShowService = Depends()):
    """Handles the specific POST HTTP request to create a new show and returns the created show as JSON if successful"""
    return service.create(show)

@router.get("/shows", response_model=list[ShowResponse])
async def read_shows(service: ShowService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all existing shows as JSON"""
    return service.get_all()

@router.get("/shows/extended", response_model=list[ShowResponseExtended])
async def read_shows(service: ShowService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all existing shows as an extended JSON with more data"""
    return service.get_all()

@router.get("/shows/{show_id}", response_model=ShowResponse)
async def read_show(show_id: int, service: ShowService = Depends()):
    """Handles the specific GET HTTP request and returns a specific show as JSON"""
    return service.get_by_id(show_id)

@router.get("/shows/{show_id}/extended", response_model=ShowResponseExtended)
async def read_show(show_id: int, service: ShowService = Depends()):
    """Handles the specific GET HTTP request and returns a specific show as an extended JSON with more data"""
    return service.get_by_id(show_id)

@router.get("/genres/{genre_id}/shows", response_model=list[ShowResponse])
async def read_shows_by_genre(genre_id: int, service: ShowService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all shows with a specific genre as JSON"""
    return service.get_by_genre(genre_id)

@router.get("/actors/{actor_id}/shows", response_model=list[ShowResponse])
async def read_shows_with_actor(actor_id: int, service: ShowService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all shows with a specific actor as JSON"""
    return service.get_with_actor(actor_id)

@router.get("/directors/{director_id}/shows", response_model=list[ShowResponse])
async def read_shows_with_director(director_id: int, service: ShowService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all shows with a specific director as JSON"""
    return service.get_with_director(director_id)

@router.post("/shows/batch", response_model=list[ShowResponse])
async def read_shows_batch(ids: list[int], service: ShowService = Depends()):
    """Handles the specific POST HTTP request and returns a list of the shows by a list of IDs as JSON"""
    return service.get_batch(ids)

@router.patch("/shows/{show_id}", response_model=ShowResponse)
async def update_show(show_id: int, show_data: ShowUpdate, service: ShowService = Depends()):
    """Handles the specific PATCH HTTP request to update an existing show and returns the updated show as JSON if successful"""
    return service.update(show_id, show_data)

@router.delete("/shows/{show_id}", response_model=dict)
async def delete_show(show_id: int, service: ShowService = Depends()):
    """Handles the specific DELETE HTTP request to delete an existing show and returns a dict as JSON if successful"""
    return service.delete(show_id)
