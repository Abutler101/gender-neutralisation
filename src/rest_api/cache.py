"""
Cacheing of API responses using Redis, keys are the hexdigest md5 hash
of the utf-8 encoded string value of api.TextRequestWrapper.text
"""
from pathlib import Path
from typing import Optional

from redis import Redis

import rest_api.api_models as api
from configuration import RedisConfig


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
