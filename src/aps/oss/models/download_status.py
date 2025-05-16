from enum import Enum

class Download_status(str, Enum):
    Complete = "complete",
    Chunked = "chunked",
    Fallback = "fallback",

