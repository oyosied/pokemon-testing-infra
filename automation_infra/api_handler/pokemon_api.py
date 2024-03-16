import requests
from automation_infra.common.common import ApiPath
from automation_infra.utils.utils import make_api_get_request


def get_pokemon_type_data():
    return make_api_get_request(ApiPath.POKEMON_TYPES)

def get_pokemon_data_by_type(type_id):
    return make_api_get_request(f'{ApiPath.POKEMONS_BY_TYPE_ID}{type_id}')
