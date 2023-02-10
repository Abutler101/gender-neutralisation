"""
Cacheing of API responses using Redis, keys are the hexdigest md5 hash
of the utf-8 encoded string value of api.TextRequestWrapper.text
"""
from hashlib import md5
from typing import Optional

from redis import Redis

import rest_api.api_models as api
from configuration import RedisConfig
from service import NeutralisationMethod


class ResultsCache:
    """Results cache using Redis, configured via env vars"""
    config: RedisConfig
    client: Redis

    def __init__(self):
        self.config = RedisConfig()
        self.client = Redis(
            host=self.config.host,
            port=self.config.port,
            password=self.config.password,
        )

    def write(self, key: str, response: api.TextResponseWrapper):
        self.client.set(key, response.json(), ex=self.config.timeout)

    def read(self, key: str) -> Optional[api.TextResponseWrapper]:
        result = self.client.get(name=key)
        if not result:
            return None
        response = api.TextResponseWrapper.parse_raw(result)
        return response

    @staticmethod
    def get_cache_key(method: NeutralisationMethod, text: str):
        """
        Calculates the cache key for a given text and neutralisation
        method. Hashes the combined method and input text
        """
        key = md5(f"{method}-{text}".encode('utf-8')).hexdigest()
        return key
