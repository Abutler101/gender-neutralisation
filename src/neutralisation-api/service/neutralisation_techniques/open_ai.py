import openai
from loguru import logger

from configuration import OpenAiConfig
from service.models import MAX_LEN


def neutralise_gender_open_ai(text: str) -> str:
    """
    Use OpenAI's LLM api to perform the neutralisation
    """
    open_ai_config = OpenAiConfig()
    openai.api_key = open_ai_config.key

    prompt_template = "replace the gendered language in the following paragraph with " \
        "gender neutral language:\n{target_text}\n\nResult: \n"

    model_input = prompt_template.format(target_text=text)

    raw_response = openai.Completion.create(
        model="text-davinci-003",
        prompt=model_input,
        temperature=0.7,
        max_tokens=MAX_LEN,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    logger.info(f"Call to OpenAI took {raw_response.response_ms}ms")
    trimmed_output: str = raw_response.choices[0].text
    return trimmed_output
