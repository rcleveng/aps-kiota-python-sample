from enum import Enum

class Type_ref(str, Enum):
    Derived = "derived",
    Dependencies = "dependencies",
    Auxiliary = "auxiliary",
    Xrefs = "xrefs",
    Includes = "includes",

