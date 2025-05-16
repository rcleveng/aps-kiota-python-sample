from enum import Enum

class DataType(str, Enum):
    List_ = "list",
    Text = "text",
    Paragraph = "paragraph",
    Numeric = "numeric",

