from enum import Enum

class PolicyKey(str, Enum):
    Transient = "transient",
    Temporary = "temporary",
    Persistent = "persistent",

