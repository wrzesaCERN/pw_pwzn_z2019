import requests
import requests_mock

from tasks.tools.metaweather import (
    get_metaweather,
    get_cities_woeid
)

url = 'https://www.metaweather.com/api/location/search'

tab_cit = [{'title': 'Warsaw', 'location_type': 'City', 'woeid': 523920, 'latt_long': '52.235352,21.009390'},
          {'title': 'Newark', 'location_type': 'City', 'woeid': 2459269, 'latt_long': '40.731972,-74.174179'}]


def test_empty():
    with requests_mock.Mocker() as m:
        m.get(url, json=[], status_code=200)
        assert get_cities_woeid("Warszawa") == {}


def test_notempty():
    with requests_mock.Mocker() as m:
        m.get(url, json=tab_cit, status_code=200)
        assert get_cities_woeid("War") == {
            "Warsaw": 523920,
            "Newark": 2459269
        }


def test_status():
    try:
        with requests_mock.Mocker() as m:
            m.get(url, status_code=404)
        get_cities_woeid("War")
    except Exception as exc:
        assert isinstance(exc, requests.exceptions.HTTPError)


def test_timeout():
    try:
        with requests_mock.Mocker() as m:
            m.get(url, exc=requests.exceptions.Timeout)
        get_cities_woeid("War", 0.1)
    except Exception as exc:
        assert isinstance(exc, requests.exceptions.Timeout)





