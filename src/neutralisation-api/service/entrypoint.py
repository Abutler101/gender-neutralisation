"""
File containing the public entry point to all gender neutralisation
methods
"""
from loguru import logger

from .models import NeutralisationMethod
from .neutralisation_techniques import neutralise_gender_open_ai


def neutralise_gender(text: str, method: NeutralisationMethod):
    if method == NeutralisationMethod.OPEN_AI:
        return neutralise_gender_open_ai(text)
    else:
        logger.error("Only Open AI driven neutralisation is currently supported")
        return text
