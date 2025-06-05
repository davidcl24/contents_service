from fastapi import APIRouter, Depends

from app.schemas.actor import ActorResponse, ActorCreate, ActorUpdate
from app.services.actor_service import ActorService

router = APIRouter(tags=["Actors"])


@router.post("/actors", response_model=ActorResponse)
async def create_actor(actor: ActorCreate, service: ActorService = Depends()):
    return service.create(actor)

@router.get("/actors", response_model=list[ActorResponse])
async def read_actors(service: ActorService = Depends()):
    return service.get_all()

@router.get("/actors/{id}", response_model=ActorResponse)
async def read_actor(actor_id: int, service: ActorService = Depends()):
    return service.get_by_id(actor_id)

@router.get("/movies/{id}/actors", response_model=list[ActorResponse])
async def read_actors_from_movie(movie_id: int, service: ActorService = Depends()):
    return service.get_from_movie(movie_id)

@router.get("/shows/{id}/actors", response_model=list[ActorResponse])
async def read_actors_from_show(show_id: int, service: ActorService = Depends()):
    return service.get_from_show(show_id)

@router.patch("/actors/{id}", response_model=ActorResponse)
async def update_actor(actor_id: int, actor_data: ActorUpdate, service: ActorService = Depends()):
    return service.update(actor_id, actor_data)

@router.delete("/actors/{id}", response_model=dict)
async def delete_actor(actor_id: int, service: ActorService = Depends()):
    return service.delete(actor_id)