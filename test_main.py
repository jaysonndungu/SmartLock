#!/usr/bin/env python3
"""
Test main file for SmartLock State Machine
Tests the FSM logic without requiring hardware.
"""

from fsm import StateMachine, State
import time


def test_state_machine():
    """Test the state machine transitions."""
    
    print("=" * 50)
    print("SmartLock State Machine Test")
    print("=" * 50)
    
    # Create state machine
    print("\n1. Creating state machine...")
    state_machine = StateMachine(initial_state=State.LOCKED)
    print(f"   Initial state: {state_machine.get_state().value}")
    
    # Setup state handlers (mock motor actions)
    print("\n2. Setting up state handlers...")
    
    def on_unlocking():
        """Mock handler for UNLOCKING state."""
        print("   🔓 Handler: Motor opening (simulated)...")
        time.sleep(0.5)  # Simulate motor running
        print("   ✅ Motor finished - triggering unlock_complete")
        state_machine.process_event("unlock_complete")
    
    def on_locking():
        """Mock handler for LOCKING state."""
        print("   🔒 Handler: Motor closing (simulated)...")
        time.sleep(0.5)  # Simulate motor running
        print("   ✅ Motor finished - triggering lock_complete")
        state_machine.process_event("lock_complete")
    
    def on_error():
        """Mock handler for ERROR state."""
        print("   ⚠️ Handler: Error occurred - stopping motor")
    
    state_machine.set_state_handler(State.UNLOCKING, on_unlocking)
    state_machine.set_state_handler(State.LOCKING, on_locking)
    state_machine.set_state_handler(State.ERROR, on_error)
    
    # Test 1: Unlock flow
    print("\n" + "=" * 50)
    print("TEST 1: Unlock Flow")
    print("=" * 50)
    print(f"Current state: {state_machine.get_state().value}")
    
    print("\n→ Triggering 'authenticated' (user wants to unlock)...")
    success = state_machine.trigger("authenticated")
    print(f"   Result: {'✅ Success' if success else '❌ Failed'}")
    print(f"   Current state: {state_machine.get_state().value}")
    
    # Wait for handler to complete
    time.sleep(1)
    print(f"\n   Final state after unlock: {state_machine.get_state().value}")
    
    # Test 2: Lock flow
    print("\n" + "=" * 50)
    print("TEST 2: Lock Flow")
    print("=" * 50)
    print(f"Current state: {state_machine.get_state().value}")
    
    print("\n→ Processing 'lock_initiated' event...")
    success = state_machine.process_event("lock_initiated")
    print(f"   Result: {'✅ Success' if success else '❌ Failed'}")
    print(f"   Current state: {state_machine.get_state().value}")
    
    # Wait for handler to complete
    time.sleep(1)
    print(f"\n   Final state after lock: {state_machine.get_state().value}")
    
    # Test 3: State checks
    print("\n" + "=" * 50)
    print("TEST 3: State Check Methods")
    print("=" * 50)
    print(f"Current state: {state_machine.get_state().value}")
    print(f"   is_locked(): {state_machine.is_locked()}")
    print(f"   is_unlocked(): {state_machine.is_unlocked()}")
    print(f"   is_locking(): {state_machine.is_locking()}")
    print(f"   is_unlocking(): {state_machine.is_unlocking()}")
    print(f"   is_error(): {state_machine.is_error()}")
    
    # Test 4: Invalid transitions
    print("\n" + "=" * 50)
    print("TEST 4: Invalid Transitions (Error Handling)")
    print("=" * 50)
    
    print("\n→ Trying to unlock when already locked (should fail)...")
    # Reset to LOCKED first
    state_machine = StateMachine(initial_state=State.LOCKED)
    success = state_machine.trigger("authenticated")
    print(f"   Result: {'✅ Success' if success else '❌ Failed (expected)'}")
    
    print("\n→ Trying to unlock again when already unlocking (should fail)...")
    success = state_machine.trigger("authenticated")
    print(f"   Result: {'✅ Success' if success else '❌ Failed (expected)'}")
    
    # Test 5: Error handling
    print("\n" + "=" * 50)
    print("TEST 5: Error Handling")
    print("=" * 50)
    
    # Go to UNLOCKING state
    state_machine = StateMachine(initial_state=State.LOCKED)
    state_machine.trigger("authenticated")
    print(f"Current state: {state_machine.get_state().value}")
    
    print("\n→ Simulating unlock error...")
    success = state_machine.process_event("unlock_error")
    print(f"   Result: {'✅ Success' if success else '❌ Failed'}")
    print(f"   Current state: {state_machine.get_state().value}")
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    print("✅ All tests completed!")
    print(f"Final state: {state_machine.get_state().value}")


if __name__ == "__main__":
    try:
        test_state_machine()
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()

