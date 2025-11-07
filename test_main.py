#!/usr/bin/env python3
"""
Simple motor test - keyboard controlled
Press 'o' to open, 'c' to close, 'q' to quit
"""

from hardware import MotorController
import time
import sys


def test_motor_keyboard():
    """Test motor with keyboard controls."""
    print("=" * 60)
    print("MOTOR KEYBOARD TEST")
    print("=" * 60)
    print("\n⚠️  Make sure motor is connected to GPIO pins!")
    print("\nControls:")
    print("  'o' + Enter - Open (motor forward)")
    print("  'c' + Enter - Close (motor backward)")
    print("  's' + Enter - Stop motor")
    print("  'q' + Enter - Quit")
    print("\nReady! Enter a command...\n")
    
    try:
        motor = MotorController()
        print("✅ Motor controller initialized\n")
        
        motor_running = False
        
        while True:
            try:
                command = input("Command (o/c/s/q): ").strip().lower()
                
                if command == 'o':
                    if not motor_running:
                        print("🔓 Opening (motor forward)...")
                        motor.open()
                        motor_running = True
                    else:
                        print("⚠️  Motor already running! Press 's' to stop first.")
                
                elif command == 'c':
                    if not motor_running:
                        print("🔒 Closing (motor backward)...")
                        motor.close()
                        motor_running = True
                    else:
                        print("⚠️  Motor already running! Press 's' to stop first.")
                
                elif command == 's':
                    if motor_running:
                        print("⏹️  Stopping motor...")
                        motor.stop()
                        motor_running = False
                    else:
                        print("⚠️  Motor not running")
                
                elif command == 'q':
                    print("\n🛑 Quitting...")
                    if motor_running:
                        motor.stop()
                    break
                
                else:
                    print("❌ Invalid command. Use 'o', 'c', 's', or 'q'")
                
                print()  # Blank line for readability
                
            except EOFError:
                # Handle Ctrl+D (Linux/Mac) or Ctrl+Z (Windows)
                print("\n🛑 Quitting...")
                if motor_running:
                    motor.stop()
                break
        
        motor.cleanup()
        print("✅ Test completed!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        try:
            if motor_running:
                motor.stop()
            motor.cleanup()
        except:
            pass
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        try:
            if 'motor_running' in locals() and motor_running:
                motor.stop()
            motor.cleanup()
        except:
            pass


if __name__ == "__main__":
    try:
        test_motor_keyboard()
    except KeyboardInterrupt:
        print("\n\n⚠️  Exiting...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
