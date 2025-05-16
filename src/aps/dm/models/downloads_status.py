from enum import Enum

class Downloads_status(str, Enum):
    Queued = "queued",
    Finished = "finished",
    Failed = "failed",
    Processing = "processing",

