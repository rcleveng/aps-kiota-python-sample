from enum import Enum

class Filter_refType(str, Enum):
    Derived = "derived",
    Dependencies = "dependencies",
    Auxiliary = "auxiliary",
    Xrefs = "xrefs",
    Includes = "includes",

