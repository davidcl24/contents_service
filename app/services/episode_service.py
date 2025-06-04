from fastapi import Depends, HTTPException
from sqlmodel import Session

from app.db.session import get_session
from app.models.episode import Episode
from app.models.show import Show
from app.schemas.episode import EpisodeCreate, EpisodeResponse, EpisodeUpdate


class EpisodeService:
    def __init__(self, session: Session = Depends(get_session())):
        self.session = session

    def create(self, episode_data: EpisodeCreate) -> EpisodeResponse:
        episode = Episode(**episode_data.model_dump())
        self.session.add(episode)
        self.session.commit()
        self.session.refresh(episode)
        return EpisodeResponse(**episode.model_dump())

    def get_all_from_show(self, show_id: int):
        show = self.session.get(Show, show_id)
        return show.episodes

    def get_by_id(self, episode_id: int):
        return self.session.get(Episode, episode_id)

    def update(self, episode_id: int, episode_data: EpisodeUpdate) -> Episode:
        episode = self.session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")

        episode_dict = episode_data.model_dump(exclude_unset=True)

        for key, value in episode_dict.items():
            setattr(episode, key, value)

        self.session.add(episode)
        self.session.commit()
        self.session.refresh(episode)
        return episode

    def delete(self, episode_id: int):
        episode = self.session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")


        self.session.delete(episode)
        self.session.commit()
        return {"message": "Episode successfully deleted"}