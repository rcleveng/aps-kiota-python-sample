from enum import Enum

class Access(str, Enum):
    Read = "Read",
    Write = "Write",
    ReadWrite = "ReadWrite",

