from pydantic import BaseModel


class TextRequestWrapper(BaseModel):
    """
    Model for submission of text for gender neutralisation
    - text (str): raw input text
    """
    text: str


class TextResponseWrapper(BaseModel):
    """
    Response model for gender neutralisation
    - input_word_count (int)
    - input_char_count (int)
    - output_word_count (int)
    - output_char_count (int)
    - truncated (bool)
    - neutralised_text (str): result of transformation
    """
    input_word_count: int
    input_char_count: int
    output_word_count: int
    output_char_count: int
    truncated: bool
    neutralised_text: str
