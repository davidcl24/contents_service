"""
It contains all of the endpoints directly related to actors
"""

from fastapi import APIRouter, Depends

from app.schemas.actor import ActorResponse, ActorCreate, ActorUpdate
from app.services.actor_service import ActorService

router = APIRouter(tags=["Actors"])


@router.post("/actors", response_model=ActorResponse)
async def create_actor(actor: ActorCreate, service: ActorService = Depends()):
    """Handles the specific POST HTTP request to create a new actor and returns the created actor as JSON if successful"""
    return service.create(actor)

@router.get("/actors", response_model=list[ActorResponse])
async def read_actors(service: ActorService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all existing actors as JSON"""
    return service.get_all()

@router.get("/actors/{actor_id}", response_model=ActorResponse)
async def read_actor(actor_id: int, service: ActorService = Depends()):
    """Handles the specific GET HTTP request and returns a specific actor as JSON"""
    return service.get_by_id(actor_id)

@router.get("/movies/{movie_id}/actors", response_model=list[ActorResponse])
async def read_actors_from_movie(movie_id: int, service: ActorService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all actors in a specific movie as JSON"""
    return service.get_from_movie(movie_id)

@router.get("/shows/{show_id}/actors", response_model=list[ActorResponse])
async def read_actors_from_show(show_id: int, service: ActorService = Depends()):
    """Handles the specific GET HTTP request and returns a list of all actors in a specific show as JSON"""
    return service.get_from_show(show_id)

@router.patch("/actors/{actor_id}", response_model=ActorResponse)
async def update_actor(actor_id: int, actor_data: ActorUpdate, service: ActorService = Depends()):
    """Handles the specific PATCH HTTP request to update an existing actor and returns the updated actor as JSON if successful"""
    return service.update(actor_id, actor_data)

@router.delete("/actors/{actor_id}", response_model=dict)
async def delete_actor(actor_id: int, service: ActorService = Depends()):
    """Handles the specific DELETE HTTP request to delete an existing actor and returns a dict as JSON if successful"""
    return service.delete(actor_id)