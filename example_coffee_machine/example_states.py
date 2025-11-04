"""
Example: Coffee Machine States
"""

from enum import Enum


class CoffeeState(Enum):
    """States for a coffee machine."""
    
    IDLE = "idle"              # Waiting for user
    SELECTING = "selecting"     # User choosing coffee type
    GRINDING = "grinding"       # Grinding coffee beans
    BREWING = "brewing"         # Brewing coffee
    READY = "ready"             # Coffee ready to serve
    ERROR = "error"             # Something went wrong

