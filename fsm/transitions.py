

from .states import State


class Transition:
    """Represents a state transition.""" 

    def __init__( 
        self,
        from_state: State,
        to_state: State,
        trigger = None
    ):
        self.from_state = from_state
        self.to_state = to_state
        self.trigger = trigger

    def can_transition(self, current_state: State, trigger = None) -> bool:

        if current_state != self.from_state:
            return False
        
        # If this transition has a trigger, it must match
        if self.trigger is not None:
            if trigger != self.trigger:
                return False
        
        # If this transition has no trigger, it's automatic (process_event)
        # and trigger parameter should be None
        return True
        
#Define all possible transitions
TRANSITIONS = {

    "start": Transition( 
        from_state = State.LOCKED,
        to_state = State.UNLOCKING,     #In this state, the doorknob is slowly let up
        trigger = "authenticated"
    ),
    "unlock_complete": Transition(
        from_state = State.UNLOCKING,    #In this state, the doorknob is held up
        to_state = State.UNLOCKED
    ),
    "lock_initiated": Transition(       #In this state, the doorknob is slowly let down
        from_state = State.UNLOCKED,
        to_state = State.LOCKING,
    ),
    "lock_complete": Transition(
        from_state = State.LOCKING,
        to_state = State.LOCKED
    ), 
    "lock_error": Transition(
        from_state = State.LOCKING,    #Error while door knob is being let down
        to_state = State.ERROR,
    ),
    "unlock_error": Transition(
        from_state = State.UNLOCKING,  #Error while door knob is being let up
        to_state = State.ERROR,
    ),
    
}