from enum import Enum

class SheetType(str, Enum):
    Open = "open",
    Surface = "surface",
    Shell = "shell",
    Wireframe = "wireframe",

