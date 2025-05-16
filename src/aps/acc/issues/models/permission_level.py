from enum import Enum

class Permission_level(str, Enum):
    Create = "create",
    Read = "read",
    Write = "write",

