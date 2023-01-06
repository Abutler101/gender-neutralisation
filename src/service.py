from enum import Enum

import openai
from loguru import logger

from configuration import OpenAiConfig


class NeutralisationMethod(str, Enum):
    OPEN_AI = "open_ai"


def neutralise_gender(text: str, method: NeutralisationMethod):
    if method == NeutralisationMethod.OPEN_AI:
        _neutralise_gender_open_ai(text)
    else:
        logger.error("Only Open AI driven neutralisation is currently supported")
        return text


def _neutralise_gender_open_ai(text: str) -> str:
    open_ai_config = OpenAiConfig()
    openai.api_key = open_ai_config.key

    prompt_template = "replace the gendered language in the following paragraph with " \
        "gender neutral language:\n{target_text}\n\nResult: \n"

    model_input = prompt_template.format(target_text=text)

    raw_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=model_input,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    trimmed_output: str = raw_response.replace(model_input, "")
    return trimmed_output
