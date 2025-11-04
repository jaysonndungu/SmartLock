"""
Example: Coffee Machine State Machine
"""

from .example_states import CoffeeState
from .example_transitions import Transition, TRANSITIONS
from typing import Dict, Callable, Optional
import threading


class CoffeeMachine:
    """State machine for coffee machine."""
    
    def __init__(self, initial_state: CoffeeState = CoffeeState.IDLE):
        """Initialize the state machine."""
        self.current_state = initial_state
        self.transitions: Dict[str, Transition] = TRANSITIONS.copy()
        self.state_handlers: Dict[CoffeeState, Callable] = {}
        self.lock = threading.Lock()
    
    def set_state_handler(self, state: CoffeeState, handler: Callable):
        """Set a function to call when entering a state."""
        self.state_handlers[state] = handler
    
    def trigger(self, trigger_name: str) -> bool:
        """
        Try to trigger a transition by name.
        Returns True if successful, False if not allowed.
        """
        with self.lock:
            # Find transition with matching trigger
            for name, transition in self.transitions.items():
                if transition.can_transition(self.current_state, trigger_name):
                    return self._execute_transition(transition)
            return False
    
    def process_event(self, event: str) -> bool:
        """
        Process an event (like "grind_complete" or "brew_complete").
        Returns True if transition happened.
        """
        with self.lock:
            if event in self.transitions:
                transition = self.transitions[event]
                if transition.can_transition(self.current_state):
                    return self._execute_transition(transition)
            return False
    
    def _execute_transition(self, transition: Transition) -> bool:
        """Actually change the state."""
        old_state = self.current_state
        self.current_state = transition.to_state
        
        print(f"State changed: {old_state.value} → {self.current_state.value}")
        
        # Call handler if one exists
        if self.current_state in self.state_handlers:
            try:
                self.state_handlers[self.current_state]()
            except Exception as e:
                print(f"Error in handler: {e}")
                return False
        
        return True
    
    def get_state(self) -> CoffeeState:
        """Get current state."""
        return self.current_state
    
    def is_ready(self) -> bool:
        """Check if coffee is ready."""
        return self.current_state == CoffeeState.READY
    
    def is_idle(self) -> bool:
        """Check if machine is idle."""
        return self.current_state == CoffeeState.IDLE


# Example usage:
if __name__ == "__main__":
    # Create state machine
    machine = CoffeeMachine()
    
    # Set handlers for different states
    def on_grinding():
        print("Starting to grind coffee beans...")
        # Simulate grinding
        import time
        time.sleep(2)
        machine.process_event("grind_complete")
    
    def on_brewing():
        print("Brewing coffee...")
        # Simulate brewing
        import time
        time.sleep(3)
        machine.process_event("brew_complete")
    
    def on_ready():
        print("☕ Coffee is ready!")
    
    machine.set_state_handler(CoffeeState.GRINDING, on_grinding)
    machine.set_state_handler(CoffeeState.BREWING, on_brewing)
    machine.set_state_handler(CoffeeState.READY, on_ready)
    
    # Simulate user interaction
    print(f"Initial state: {machine.get_state().value}")
    
    machine.trigger("start")        # IDLE → SELECTING
    machine.trigger("select")       # SELECTING → GRINDING (triggers handler)
    # Handler will call process_event("grind_complete") automatically
    # Then GRINDING → BREWING (triggers handler)
    # Handler will call process_event("brew_complete") automatically
    # Then BREWING → READY (triggers handler)
    
    print(f"Final state: {machine.get_state().value}")

