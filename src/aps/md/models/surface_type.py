from enum import Enum

class SurfaceType(str, Enum):
    Bounded = "bounded",
    Trimmed = "trimmed",
    Wireframe = "wireframe",

