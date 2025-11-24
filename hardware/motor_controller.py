from gpiozero import Motor
from config.settings import MOTOR_PIN, IN1_PIN, IN2_PIN, SPEED

class MotorController:
    def __init__(self):
        print(f"DEBUG: Initializing motor with pins: IN1={IN1_PIN}, IN2={IN2_PIN}, ENABLE={MOTOR_PIN}, SPEED={SPEED}")
        # For H-bridge with separate enable pin (like L298N)
        self.motor = Motor(
            forward = IN1_PIN,   # Pin 23 - forward direction
            backward = IN2_PIN, # Pin 24 - backward direction
            enable = MOTOR_PIN, # Pin 18 - enable pin (PWM for speed control)
            pwm = True
        )
        print("DEBUG: Motor initialized successfully")

    def open(self):
        """Open/unlock door - rack goes up (backward gear)."""
        print(f"DEBUG: Motor.open() called - running backward at speed {SPEED}")
        self.motor.backward(SPEED)
        print("DEBUG: Motor.backward() executed")

    def close(self):
        """Close/lock door - rack goes down (forward gear)."""
        print(f"DEBUG: Motor.close() called - running forward at speed {SPEED}")
        self.motor.forward(SPEED)
        print("DEBUG: Motor.forward() executed")

    def stop(self):
        print("DEBUG: Motor.stop() called")
        self.motor.stop()

    def cleanup(self):
        self.stop()
        self.motor.close()
        print("DEBUG: Motor cleaned up")


