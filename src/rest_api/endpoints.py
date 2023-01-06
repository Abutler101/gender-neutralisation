from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED
from loguru import logger

import rest_api.api_models as api
from service import neutralise_gender, NeutralisationMethod

neutralisation_router = APIRouter()

@neutralisation_router.post(
    "/",
    description=""" Some Description """,
    response_model=api.TextResponseWrapper,
    status_code=HTTP_201_CREATED,
)
def neutralise_text_gender(
    input_text: api.TextRequestWrapper,
) -> api.TextResponseWrapper:
    neutralised_text = neutralise_gender(input_text.text, NeutralisationMethod.OPEN_AI)
    response = api.TextResponseWrapper(
        input_word_count=len(input_text.text.split()),
        input_char_count=len(input_text.text),
        output_word_count=len(neutralised_text.split()),
        output_char_count=len(neutralised_text),
        neutralised_text=neutralised_text
    )

    return response
