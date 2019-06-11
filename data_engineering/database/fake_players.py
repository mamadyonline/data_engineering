from faker import Faker
import random

COUNTRIES = ['Argentina', 'Portugal', 'France', 'Brazil',
             'England', 'Belgium', 'Italy', 'Spain', 'Germany',
             'Ivory coast', 'Guinea', 'Senegal', 'Ghana',
             'Nigeria', 'Cameroun', 'Egypt', 'Morocco', 'Algeria',
             'USA', 'Croatia', 'Sweden', 'Columbia', 'Netherlands',
             'Danemark', 'Ireland', 'Switzerland']

CLUBS = ['Barcelona', 'Real Madrid', 'Juventus', 'Liverpool', 'Ajax',
         'Totenham', 'PSG', 'Lyon', 'Napoli',
         'Olympique de Marseille', 'Valence FC',
         'Manchester United', 'Manchester City', 'Chealsea',
         'Athlético Madrid','Bayern de Munich', 'Dortmund',
         'Arsenal', 'AC Milan', 'Roma', 'Inter', 'Monaco', 'Sevilla']

fake = Faker()


def generate_fake_player():
    d = dict()
    d['name'] = lambda: fake.name_male()
    d['nationality'] = lambda: random.choice(COUNTRIES)
    d['club'] = lambda: random.choice(CLUBS)
    d['total_scored_goals'] = lambda: random.randint(0, 700)
    d['total_personal_trophies'] = lambda: random.randint(0, 20)
    d['active'] = lambda: random.choice([False, True])
    return {k: d[k]() for k in d.keys()}
