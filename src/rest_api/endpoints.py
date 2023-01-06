from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED
from loguru import logger

import rest_api.api_models as api
from service import neutralise_gender, NeutralisationMethod, MAX_LEN

neutralisation_router = APIRouter(tags=["gender-neutralisation"])


@neutralisation_router.post(
    "/",
    description=f"Apply a method to neutralise gendered language within "
                f"a text up to a max of {MAX_LEN} words",
    response_model=api.TextResponseWrapper,
    status_code=HTTP_201_CREATED,
)
def neutralise_text_gender(
    input_text: api.TextRequestWrapper,
) -> api.TextResponseWrapper:
    truncated = False
    if len(input_text.text.split()) > MAX_LEN:
        truncated = True
    cleaned=input_text.text.strip()
    neutralised_text = neutralise_gender(cleaned, NeutralisationMethod.OPEN_AI)
    response = api.TextResponseWrapper(
        input_word_count=len(input_text.text.split()),
        input_char_count=len(input_text.text),
        output_word_count=len(neutralised_text.split()),
        output_char_count=len(neutralised_text),
        truncated=truncated,
        neutralised_text=neutralised_text
    )

    return response
