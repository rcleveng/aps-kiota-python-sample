from enum import Enum

class OutputType(str, Enum):
    Svf = "svf",
    Svf2 = "svf2",
    Thumbnail = "thumbnail",
    Stl = "stl",
    Step = "step",
    Iges = "iges",
    Obj = "obj",
    Ifc = "ifc",
    Dwg = "dwg",
    Fbx = "fbx",

