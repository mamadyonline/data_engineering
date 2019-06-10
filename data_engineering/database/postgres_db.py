"""Module to handle data base connection to PostgreSQL via SQLAlchemy"""
from typing import List

from data_engineering.database.base import Base, Session, data_base
from data_engineering.database.players import Player


class DataBase:

    def __init__(self):
        # create a session and register players table
        self.session = Session()
        Base.metadata.create_all(data_base)

    def drop_all(self):
        self.session.query(Player).delete()
        self.session.commit()

    def add_new_player(self, player: Player):
        self.session.add(player)
        self.session.commit()

    def add_players(self, players: List[Player]):
        for player in players:
            self.session.add(player)
        self.session.commit()

    def read_all(self):
        return self.session.query(Player).all()

    def delete_entry(self, player):
        self.session.query(Player).filter(Player == player).delete()
        self.session.commit()

    def get_players_from_club(self, club: str = 'Barcelona'):
        players = self.session.query(Player).filter(Player.club == club).all()
        return players

    def delete_players_from_club(self, club: str = 'PSG'):
        self.session.query(Player).filter(Player.club == club).delete()
        self.session.commit()

    def get_top_scorers(self):
        top_scorers = self.session.query(Player).filter(Player.total_scored_goals >= 600).all()
        return top_scorers

    def close(self):
        self.session.close()


