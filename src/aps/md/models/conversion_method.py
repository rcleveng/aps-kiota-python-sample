from enum import Enum

class ConversionMethod(str, Enum):
    Legacy = "legacy",
    Modern = "modern",
    V3 = "v3",
    V4 = "v4",

