import click
import requests

API_URL = "https://es.wikipedia.org/api/rest_v1/page/random/summary"


def random_page():
    try:
        with requests.get(API_URL) as response:
            response.raise_for_status()
            return response.json()
    except requests.RequestException as err:
        message = str(err)
        raise click.ClickException(message)
