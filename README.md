# SmartLock

SmartLock is a system that allows you to lock and unlock your door using your phone. It utilizes a Raspberry Pi 5 to control the lock through a finite state machine (FSM) architecture.

## Project Information

- **Version:** 1.0.0
- **Author:** Jayson Ndungu
- **Description:** SmartLock is a system that allows you to lock and unlock your door using your phone. It utilizes a raspberry pi 5 to control the lock.

## Project Structure

```
smart-lock/
├── config/
│   └── settings.py          # Configuration and pin assignments
├── hardware/
│   ├── __init__.py
│   ├── motor_controller.py  # Motor control using GPIOZero
│   └── bluetooth_manager.py # Bluetooth connections and command parsing
├── fsm/
│   ├── __init__.py
│   ├── states.py            # System state enumerations
│   ├── transitions.py       # Transition conditions and triggers
│   └── state_machine.py     # FSM logic and state transitions
├── test_main.py             # Test file for state machine (no hardware required)
└── README.md
```

## Hardware Requirements

- Raspberry Pi 5
- Motor controller (L298N H-Bridge or similar)
- DC Motor for lock mechanism
- Bluetooth module (for phone connectivity)

## Pin Configuration

Default pin assignments (configurable in `config/settings.py`):
- `MOTOR_PIN = 18` (Enable pin)
- `IN1_PIN = 23` (Direction control - forward)
- `IN2_PIN = 24` (Direction control - backward)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jaysonndungu/SmartLock.git
cd smart-lock
```

2. Install required dependencies:
```bash
pip install gpiozero pybluez
```

Or use requirements.txt (if available):
```bash
pip install -r requirements.txt
```

3. Configure settings in `config/settings.py` if needed.

## State Machine

The SmartLock uses a finite state machine (FSM) to manage lock states:

### States
- **LOCKED**: Door is locked
- **UNLOCKING**: Door is currently unlocking (motor running)
- **UNLOCKED**: Door is unlocked
- **LOCKING**: Door is currently locking (motor running)
- **ERROR**: Error state

### Transitions
- `trigger("authenticated")` → LOCKED → UNLOCKING (user command)
- `process_event("unlock_complete")` → UNLOCKING → UNLOCKED (automatic)
- `process_event("lock_initiated")` → UNLOCKED → LOCKING (automatic)
- `process_event("lock_complete")` → LOCKING → LOCKED (automatic)
- Error transitions for handling failures

## Usage

### Testing (No Hardware Required)

Test the state machine logic without hardware:

```bash
python test_main.py
```

This will run through all state transitions and handlers to verify the FSM logic.

### Running the Full System

1. Ensure all hardware is connected according to pin configuration
2. Run the main application:
```bash
python main.py
```

3. Connect via Bluetooth and send commands:
   - `"unlock"` - Unlock the door
   - `"lock"` - Lock the door
   - `"status"` - Check current state

### Example Usage

```python
from fsm import StateMachine, State
from hardware import MotorController

# Create instances
motor = MotorController()
state_machine = StateMachine(initial_state=State.LOCKED)

# Setup handlers
def on_unlocking():
    motor.open()
    time.sleep(2)
    motor.stop()
    state_machine.process_event("unlock_complete")

state_machine.set_state_handler(State.UNLOCKING, on_unlocking)

# Trigger unlock
state_machine.trigger("authenticated")
```

## Development

### Testing
- Use `test_main.py` to test state machine logic without hardware
- All state transitions and handlers are tested

### Code Structure
- **FSM Module**: Handles all state management and transitions
- **Hardware Module**: Abstracts motor and Bluetooth control
- **Config Module**: Centralized configuration

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

## Repository

GitHub: https://github.com/jaysonndungu/SmartLock
