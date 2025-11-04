"""
Example Coffee Machine State Machine
Use this as a reference for your SmartLock implementation.
"""

from .example_states import CoffeeState
from .example_transitions import Transition, TRANSITIONS
from .example_state_machine import CoffeeMachine

__all__ = ['CoffeeState', 'Transition', 'TRANSITIONS', 'CoffeeMachine']

