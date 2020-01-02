import pathlib
from typing import Optional, Union, List
from urllib.parse import urljoin
import requests
import csv
import os

API_URL = 'https://www.metaweather.com/api/'


def get_city_data(
        woeid: int, year: int, month: int,
        path: Optional[Union[str, pathlib.Path]] = None,
        timeout: float = 5.
) -> (str, List[str]):
    path_zero = pathlib.Path.cwd()
    if path is None:
        path_final = path_zero / f"{woeid}_{year}_{month:02}"
    elif type(path) == pathlib.PosixPath:
        path_final = path
    elif type(path) == str:
        path_final = pathlib.PosixPath(path) / f"{woeid}_{year}_{month:02}"
    if not os.path.exists(os.path.dirname(str(path_final)+ "/")):
        os.makedirs(os.path.dirname(str(path_final) + "/"))

    files = []
    for day in range(1,32):
        loc_url = urljoin(API_URL,f"location/{woeid}/{year}/{month}/{day}")
        response = requests.get(loc_url, timeout=timeout)
        data = None
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f'The problem is here: {e}, communication or sth like that ...')

        try:
            data = response.json()
        except requests.exceptions.Timeout:
            raise RuntimeError

        if data:
            with open(path_final / f'{year}_{month:02}_{day:02}.csv', 'w') as f:
                writer = csv.DictWriter(f, delimiter=',', quotechar='"', fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            files.append(path_final / str(day))

    return str(path_final), files

if __name__ == '__main__':
    _path = pathlib.Path.cwd()
    expected_path = _path / '523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3)
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert str(expected_path) == dir_path

    expected_path = 'weather_data/523920_2017_03'
    dir_path, file_paths = get_city_data(523920, 2017, 3, path='weather_data')
    assert len(file_paths) == 31
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path

    expected_path = 'weather_data/523920_2012_12'
    dir_path, file_paths = get_city_data(523920, 2012, 12, path='weather_data')
    assert len(file_paths) == 0
    assert pathlib.Path(dir_path).is_dir()
    assert expected_path == dir_path
