from enum import Enum

class Status(str, Enum):
    Draft = "draft",
    Open = "open",
    Pending = "pending",
    In_progress = "in_progress",
    In_review = "in_review",
    Completed = "completed",
    Not_approved = "not_approved",
    In_dispute = "in_dispute",
    Closed = "closed",

