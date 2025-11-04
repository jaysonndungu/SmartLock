"""
Example: Coffee Machine Transitions
"""

from .example_states import CoffeeState
from typing import Optional, Callable


class Transition:
    """Represents a state transition."""
    
    def __init__(
        self,
        from_state: CoffeeState,
        to_state: CoffeeState,
        trigger: Optional[str] = None,
        condition: Optional[Callable[[], bool]] = None
    ):
        self.from_state = from_state
        self.to_state = to_state
        self.trigger = trigger
        self.condition = condition
    
    def can_transition(self, current_state: CoffeeState, trigger: Optional[str] = None) -> bool:
        """Check if transition is allowed."""
        # Must be in the correct starting state
        if current_state != self.from_state:
            return False
        
        # If trigger specified, must match
        if self.trigger and trigger != self.trigger:
            return False
        
        # If condition specified, must pass
        if self.condition and not self.condition():
            return False
        
        return True


# Define all possible transitions
TRANSITIONS = {
    # User starts interaction
    "start": Transition(
        from_state=CoffeeState.IDLE,
        to_state=CoffeeState.SELECTING,
        trigger="start"
    ),
    
    # User selects coffee type
    "select_coffee": Transition(
        from_state=CoffeeState.SELECTING,
        to_state=CoffeeState.GRINDING,
        trigger="select"
    ),
    
    # Grinding completes
    "grind_complete": Transition(
        from_state=CoffeeState.GRINDING,
        to_state=CoffeeState.BREWING
    ),
    
    # Brewing completes
    "brew_complete": Transition(
        from_state=CoffeeState.BREWING,
        to_state=CoffeeState.READY
    ),
    
    # User takes coffee
    "take_coffee": Transition(
        from_state=CoffeeState.READY,
        to_state=CoffeeState.IDLE,
        trigger="take"
    ),
    
    # Error during grinding
    "grind_error": Transition(
        from_state=CoffeeState.GRINDING,
        to_state=CoffeeState.ERROR
    ),
    
    # Error during brewing
    "brew_error": Transition(
        from_state=CoffeeState.BREWING,
        to_state=CoffeeState.ERROR
    ),
    
    # Reset from error
    "reset": Transition(
        from_state=CoffeeState.ERROR,
        to_state=CoffeeState.IDLE,
        trigger="reset"
    ),
    
    # Cancel from selecting
    "cancel": Transition(
        from_state=CoffeeState.SELECTING,
        to_state=CoffeeState.IDLE,
        trigger="cancel"
    ),
}

