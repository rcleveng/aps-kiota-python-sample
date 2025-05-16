from enum import Enum

class SolidType(str, Enum):
    Solid = "solid",
    Surface = "surface",
    Wireframe = "wireframe",

