from .states import State
from transitions import Transition, TRANSITIONS
import threading

class StateMachine:

    def __init(self, initial_state: State = State.LOCKED):
        self.current_state = initial_state
        self.transitions = TRANSITIONS.copy()
        self.state_handler = {}
        self.lock = threading.Lock()

    def set_state_handler(self, state: State, handler):
        self.state_handler[state] = handler


    def get_state(self):
        return self.current_state

    
    #Trigger a transition
    def trigger(self, trigger_name: str):

        with self.lock:
            for name, transition in self.transitions.items():
                if transition.can_transition(self.current_state, trigger_name):
                    return self._execute_transition(transition)
            return False
    
    def process_event(self, event: str):
        with self.lock:
            if event in self.transitions:
                transition = self.transitions[event]
                if transition.can_transition(self.current_state):
                    return self._execute_transition(transition)
            return False

    def _execute_transition(self, transition: Transition):
        old_state = self.current_state
        self.current_state = transition.to_state

        print(f"State changed: {old_state.value} -> {self.current_state.value}")

        if self.current_state in self.state_handler:
            try:
                self.state_handler[self.current_state]()
            except Exception as e:
                print(f"Error in handler: {e}")
                return False
        return True


    def is_locked(self):
        return self.current_state == State.LOCKED
    
    def is_unlocked(self):
        return self.current_state == State.UNLOCKED
    
    def is_error(self):
        return self.current_state == State.ERROR
    
    def is_unlocking(self):
        return self.current_state == State.UNLOCKING
    
    def is_locking(self):
        return self.current_state == State.LOCKING
    
    