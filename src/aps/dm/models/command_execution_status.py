from enum import Enum

class Command_execution_status(str, Enum):
    Accepted = "accepted",
    Committed = "committed",
    Complete = "complete",
    Failed = "failed",

