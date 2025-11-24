from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from app.db.session import get_session
from app.models.episode import Episode
from app.models.show import Show
from app.schemas.episode import EpisodeCreate, EpisodeResponse, EpisodeUpdate


class EpisodeService:
    """It contains the CRUD for the actors table in the DB"""
    def __init__(self, session: Session = Depends(get_session)):
        """Instantiates an object of the EpisodeService class with a session to communicate with the DB"""
        self.session = session

    def create(self, episode_data: EpisodeCreate) -> EpisodeResponse:
        """Creates a new episode based on the received schema"""
        episode = Episode(**episode_data.model_dump())
        self.session.add(episode)
        self.session.commit()
        self.session.refresh(episode)
        return EpisodeResponse(**episode.model_dump())

    def get_all_from_show(self, show_id: int):
        """Returns a list of all episodes in a show"""
        show = self.session.get(Show, show_id)
        return show.episodes

    def get_from_show_by_season(self, show_id: int, season_num: int):
        """Returns a list of all episodes in a show and a season"""
        query = select(Episode).where(Episode.show_id == show_id).where(Episode.season_num == season_num)
        return self.session.exec(query).all()

    def get_by_id(self, episode_id: int):
        """Returns only the desired episode"""
        return self.session.get(Episode, episode_id)

    def update(self, episode_id: int, episode_data: EpisodeUpdate) -> Episode:
        """Updates an existing episode based on the received schema"""
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
        """Removes the desired episode from the DB"""
        episode = self.session.get(Episode, episode_id)
        if not episode:
            raise HTTPException(status_code=404, detail="Episode not found")


        self.session.delete(episode)
        self.session.commit()
        return {"message": "Episode successfully deleted"}