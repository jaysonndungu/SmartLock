from gpiozero import Motor
from config.settings import MOTOR_PIN, IN1_PIN, IN2_PIN, SPEED

class MotorController:
    def __init__(self):
        self.motor = Motor(
            forward = IN1_PIN, #Pin 23
            backward = IN2_PIN, #Pin 24
            enable = MOTOR_PIN, #Pin 18
            pwm = True
        )

    def open(self):
        """Open/unlock door - rack goes up (backward gear)."""
        self.motor.backward(SPEED)

    def close(self):
        """Close/lock door - rack goes down (forward gear)."""
        self.motor.forward(SPEED)

    def stop(self):
        self.motor.stop()

    def cleanup(self):
        self.stop()
        self.motor.close()


