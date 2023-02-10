from enum import Enum

# token cap
MAX_LEN = 512


class NeutralisationMethod(str, Enum):
    OPEN_AI = "open_ai"
