#!/usr/bin/env python3
"""
Test file for SmartLock Hardware and State Machine
Tests motor controller and FSM with actual hardware.
"""

from hardware import MotorController
from fsm import StateMachine, State
import time


def test_motor_only():
    """Test motor hardware directly (no state machine)."""
    print("=" * 60)
    print("MOTOR HARDWARE TEST")
    print("=" * 60)
    print("\n Make sure motor is connected to GPIO pins!")
    print("Press Ctrl+C to stop early\n")
    
    try:
        motor = MotorController()
        print("✅ Motor controller initialized")
        
        # Test forward (unlock)
        print("\n" + "-" * 60)
        print("TEST 1: Motor Forward (Unlock)")
        print("-" * 60)
        print("🔓 Starting motor forward...")
        motor.open()
        print("   Motor running forward (2 seconds)...")
        time.sleep(2)
        motor.stop()
        print("✅ Motor stopped")
        
        # Wait a moment
        time.sleep(1)
        
        # Test backward (lock)
        print("\n" + "-" * 60)
        print("TEST 2: Motor Backward (Lock)")
        print("-" * 60)
        print("🔒 Starting motor backward...")
        motor.close()
        print("   Motor running backward (2 seconds)...")
        time.sleep(2)
        motor.stop()
        print("✅ Motor stopped")
        
        print("\n" + "=" * 60)
        print("✅ Motor test completed successfully!")
        print("=" * 60)
        
        motor.cleanup()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        motor.stop()
        motor.cleanup()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        try:
            motor.cleanup()
        except:
            pass


def test_with_state_machine():
    """Test motor with state machine integration."""
    print("\n" + "=" * 60)
    print("STATE MACHINE + MOTOR TEST")
    print("=" * 60)
    print("\n  Make sure motor is connected to GPIO pins!")
    print("Press Ctrl+C to stop early\n")
    
    try:
        motor = MotorController()
        state_machine = StateMachine(initial_state=State.LOCKED)
        
        print(f"Initial state: {state_machine.get_state().value}")
        
        # Setup handlers with actual motor
        def on_unlocking():
            """Handler for UNLOCKING state - uses real motor."""
            print("Handler: Motor opening...")
            motor.open()
            time.sleep(2)  # Motor runs for 2 seconds
            motor.stop()
            print("✅ Motor finished - triggering unlock_complete")
            state_machine.process_event("unlock_complete")
        
        def on_locking():
            """Handler for LOCKING state - uses real motor."""
            print("🔒 Handler: Motor closing...")
            motor.close()
            time.sleep(2)  # Motor runs for 2 seconds
            motor.stop()
            print("✅ Motor finished - triggering lock_complete")
            state_machine.process_event("lock_complete")
        
        state_machine.set_state_handler(State.UNLOCKING, on_unlocking)
        state_machine.set_state_handler(State.LOCKING, on_locking)
        
        # Test unlock flow
        print("\n" + "-" * 60)
        print("TEST: Unlock Flow (LOCKED → UNLOCKING → UNLOCKED)")
        print("-" * 60)
        print(f"Current state: {state_machine.get_state().value}")
        
        print("\n→ Triggering unlock...")
        success = state_machine.trigger("authenticated")
        print(f"   Result: {'✅ Success' if success else '❌ Failed'}")
        
        # Wait for handler to complete
        time.sleep(3)
        print(f"\n   Final state: {state_machine.get_state().value}")
        
        # Wait a moment
        time.sleep(1)
        
        # Test lock flow
        print("\n" + "-" * 60)
        print("TEST: Lock Flow (UNLOCKED → LOCKING → LOCKED)")
        print("-" * 60)
        print(f"Current state: {state_machine.get_state().value}")
        
        print("\n→ Triggering lock...")
        success = state_machine.process_event("lock_initiated")
        print(f"   Result: {'✅ Success' if success else '❌ Failed'}")
        
        # Wait for handler to complete
        time.sleep(3)
        print(f"\n   Final state: {state_machine.get_state().value}")
        
        print("\n" + "=" * 60)
        print("✅ State machine + motor test completed!")
        print("=" * 60)
        
        motor.cleanup()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        motor.stop()
        motor.cleanup()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        try:
            motor.cleanup()
        except:
            pass


def main():
    """Main test menu."""
    print("\n" + "=" * 60)
    print("SmartLock Hardware Test")
    print("=" * 60)
    print("\nChoose a test:")
    print("1. Motor only (simple forward/backward test)")
    print("2. State machine + Motor (full integration test)")
    print("3. Both tests")
    print("0. Exit")
    
    choice = input("\nEnter choice (0-3): ").strip()
    
    if choice == "1":
        test_motor_only()
    elif choice == "2":
        test_with_state_machine()
    elif choice == "3":
        test_motor_only()
        time.sleep(2)
        test_with_state_machine()
    elif choice == "0":
        print("Exiting...")
    else:
        print("Invalid choice. Running motor test by default...")
        test_motor_only()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Exiting...")
    except Exception as e:
        print(f"\n Error: {e}")
        import traceback
        traceback.print_exc()
