import json

import requests
from loguru import logger


def make_api_get_request(url):
    try:
        logger.info(f"Making GET request to '{url}'")
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX or 5XX
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8', "Expected JSON response"
        data = response.json()
        logger.info(f"Response from '{url}':\n{data}")
        return data
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        raise
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error occurred: {e}")
        raise
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout error occurred: {e}")
        raise
    except requests.exceptions.RequestException as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise
    except AssertionError as e:
        logger.error(f"Assertion error occurred: {e}")
        raise