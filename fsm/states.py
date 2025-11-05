from enum import Enum

class State(Enum):
    LOCKED = "locked"                # Door is locked
    UNLOCKING = "unlocking"          # Door is unlocking
    UNLOCKED = "unlocked"            # Door is unlocked
    LOCKING = "locking"              # Door is locking
    ERROR = "error"                  # Error occurred
