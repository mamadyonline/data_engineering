"""Create players class and define its characteristics"""

from data_engineering.database.base import Base
from sqlalchemy import String, Integer, Column, Boolean


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    nationality = Column('nationality',String)
    club = Column('club', String)  # current if still active, last club if retired
    total_scored_goals = Column('total_scored_goals', Integer)
    total_personal_trophies = Column('total_personal_goals', Integer)
    active = Column('active', Boolean)

    def __init__(self, name, nationality, club, total_scored_goals, total_personal_trophies, active):
        """Initialize without the id component as it is taken care of automatically."""
        self.name = name
        self.nationality = nationality
        self.club = club
        self.total_scored_goals = total_scored_goals
        self.total_personal_trophies = total_personal_trophies
        self.active = active

    def __repr__(self):
        """Prettify when we print a player"""
        if self.active:
            to_print = f"<Player({self.name} from {self.nationality}, " \
                f"currently playing at {self.club} with {self.total_scored_goals} goals)>"
        else:
            to_print = f"<Player({self.name} from {self.nationality}, " \
                f"retired while at {self.club}) with {self.total_scored_goals} goals>"
        return to_print
