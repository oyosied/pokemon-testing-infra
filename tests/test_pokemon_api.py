import pytest

from automation_infra.api_handler.pokemon_api import get_pokemon_type_data, get_pokemon_data_by_type
from automation_infra.common.common import ApiPath, HEAVIEST_POKEMONS
from automation_infra.utils.utils import make_api_get_request


@pytest.mark.parametrize("type_url", [f'{ApiPath.POKEMONS_BY_TYPE_ID}1', ApiPath.POKEMON_TYPES])
def test_pokemon_json_response(type_url):
    data = make_api_get_request(type_url)
    assert isinstance(data, dict)


@pytest.mark.parametrize("type_url", [ApiPath.POKEMON_TYPES])
def test_pokemon_types(type_url):
    data = make_api_get_request(type_url)
    assert len(data['results']) == 20


def test_fire_type_pokemon():
    data = get_pokemon_type_data()
    fire_type = next((item for item in data['results'] if item['name'] == 'fire'), None)
    assert fire_type is not None
    fire_type_data = get_pokemon_data_by_type(fire_type['name'])
    pokemon_names = [pokemon['pokemon']['name'] for pokemon in fire_type_data['pokemon']]
    assert 'charmander' in pokemon_names
    assert 'bulbasaur' not in pokemon_names


def test_heaviest_fire_pokemon():
    fire_type_data = get_pokemon_data_by_type('fire')
    fire_pokemon_weights = {pokemon['pokemon']['name']: pokemon['pokemon']['url'] for pokemon in
                            fire_type_data['pokemon']}
    for name, url in fire_pokemon_weights.items():
        if name in HEAVIEST_POKEMONS:
            pokemon_data = make_api_get_request(url)
            assert pokemon_data['weight'] == HEAVIEST_POKEMONS[name]
