from enum import Enum

class State(Enum):
    AUTHENTICATING = "authenticating"
    LOCKED = "locked"
    UNLOCKING = "unlocking"
    UNLOCKED = "unlocked"
    LOCKING = "locking"
    ERROR = "error" 
