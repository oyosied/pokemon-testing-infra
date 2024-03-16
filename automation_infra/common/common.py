from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
CONFIG_FILE = 'config.json'

class ApiPath:
    BASE_URL = 'https://pokeapi.co/api/v2/'
    POKEMON_TYPES = f'{BASE_URL}type'
    POKEMONS_BY_TYPE_ID = f'{BASE_URL}type/'


HEAVIEST_POKEMONS = {
    'charizard-gmax': 10000,
    'cinderace-gmax': 10000,
    'coalossal-gmax': 10000,
    'centiskorch-gmax': 10000,
    'groudon-primal': 9997
}
