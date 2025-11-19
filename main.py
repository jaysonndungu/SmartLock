#!/usr/bin/env python3
"""
SmartLock Main Application
Handles the unlock -> wait -> lock sequence using state machine.
"""

from hardware import MotorController
from fsm import StateMachine, State
import time


def unlock_door():
    """
    Main unlock function.
    Unlocks door (rack up), waits 5 seconds, then locks (rack down).
    Uses state machine with handlers.
    """
    motor = MotorController()
    state_machine = StateMachine(initial_state=State.LOCKED)
    
    # Setup state handlers
    def on_unlocking():
        """Handler for UNLOCKING state - lifts door handle."""
        print("🔓 Unlocking door (rack up, handle lifts)...")
        motor.open()  # open() = unlock = rack goes up
        time.sleep(2)  # Motor runs for 2 seconds to lift handle
        motor.stop()
        print("✅ Door unlocked - handle is up")
        # Trigger transition to UNLOCKED
        state_machine.process_event("unlock_complete")
    
    def on_unlocked():
        """Handler for UNLOCKED state - wait then auto-lock."""
        print("⏳ Waiting 5 seconds (door open)...")
        time.sleep(5)
        # Automatically trigger lock after wait
        print("🔒 Auto-locking door (rack down, handle lowers)...")
        state_machine.process_event("lock_initiated")
    
    def on_locking():
        """Handler for LOCKING state - lowers door handle."""
        print("🔒 Locking door (rack down, handle lowers)...")
        motor.close()  # close() = lock = rack goes down
        time.sleep(2)  # Motor runs for 2 seconds to lower handle
        motor.stop()
        print("✅ Door locked - handle is down")
        # Trigger transition to LOCKED
        state_machine.process_event("lock_complete")
    
    # Register handlers
    state_machine.set_state_handler(State.UNLOCKING, on_unlocking)
    state_machine.set_state_handler(State.UNLOCKED, on_unlocked)
    state_machine.set_state_handler(State.LOCKING, on_locking)
    
    try:
        # Start the sequence by triggering unlock
        print("Starting unlock sequence...")
        success = state_machine.trigger("authenticated")
        
        if success:
            # Wait for the complete sequence to finish
            # (unlock -> wait -> lock)
            time.sleep(10)  # 2 sec unlock + 5 sec wait + 2 sec lock + buffer
            print(f"Sequence complete. Final state: {state_machine.get_state().value}")
        else:
            print("Failed to start unlock sequence")
        
    except KeyboardInterrupt:
        print("\n  Interrupted - stopping motor")
        motor.stop()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        motor.stop()
    finally:
        motor.cleanup()


if __name__ == "__main__":
    unlock_door()
