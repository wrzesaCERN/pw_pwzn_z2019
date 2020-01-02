import requests
from urllib.parse import urljoin
from json import JSONDecodeError

API_URL = 'https://www.metaweather.com/api/'

def get_cities_woeid(query: str, timeout: float = 5.):

    loc_url = urljoin(API_URL,'location/search')
    response = requests.get(loc_url, params=dict(query=query), timeout=timeout)
    output = {}

    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        print(f'The problem is here: {e}')

    try:
        cities_json = response.json()
        for beautiful_city in cities_json:
            output[beautiful_city['title']] = beautiful_city['woeid']

    except requests.exceptions.Timeout:
        raise RuntimeError

    return output


if __name__ == '__main__':
    assert get_cities_woeid('Warszawa') == {}
    assert get_cities_woeid('War') == {
        'Warsaw': 523920,
        'Newark': 2459269,
    }
    try:
        get_cities_woeid('Warszawa', 0.1)
    except Exception as exc:
        isinstance(exc, requests.exceptions.Timeout)
