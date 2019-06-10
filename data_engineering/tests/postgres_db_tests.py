"""Test data base module"""
import unittest

from data_engineering.database.fake_players import generate_fake_player
from data_engineering.database.players import Player
from data_engineering.database.postgres_db import DataBase


class TestDB(unittest.TestCase):
    def setUp(self) -> None:
        """Instantiate a class to work with"""
        self.postgres = DataBase()

    def tearDown(self) -> None:
        """empty table and close connection"""
        self.postgres.drop_all()
        self.postgres.close()

    def test_insert_one_player(self):
        """Insert one player"""
        messi = Player(name='Lionel Messi', nationality='Argentina',
                       club='Barcelona', total_scored_goals=686,
                       total_personal_trophies=15, active=True)
        self.postgres.add_new_player(messi)
        db_content = [player for player in self.postgres.read_all()]
        self.assertEqual(1, len(db_content))
        self.assertEqual(messi, db_content[0])

    def test_insert_more_than_one_player(self):
        # create players
        messi = Player(name='Lionel Messi', nationality='Argentina',
                       club='Barcelona', total_scored_goals=686,
                       total_personal_trophies=15, active=True)
        cristiano = Player(name='Cristiano Ronaldo', nationality='Portugal',
                           club='Juventus', total_scored_goals=680,
                           total_personal_trophies=18, active=True)
        players = [messi, cristiano]
        NB = 1000
        fake_players = [generate_fake_player() for _ in range(NB)]
        players.extend([Player(**player) for player in fake_players])
        # add them all
        self.postgres.add_players(players)
        db_content = [player for player in self.postgres.read_all()]
        self.assertEqual(NB + 2, len(db_content))
        self.assertEqual(messi, db_content[0])
        self.assertEqual(cristiano, db_content[1])

        # get players from Barcelona: should contain at least Messi
        barca_players = [b_p for b_p in self.postgres.get_players_from_club('Barcelona')]
        self.assertGreaterEqual(len(barca_players), 1)
        self.assertIn(messi, barca_players)

        # get top scorers: should contain at least Messi and Cristiano
        top_scorers = [t_p for t_p in self.postgres.get_top_scorers()]
        self.assertGreaterEqual(len(top_scorers), 2)
        self.assertIn(messi, top_scorers)
        self.assertIn(cristiano, top_scorers)
