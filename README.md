# SmartLock

SmartLock is a system that allows you to lock and unlock your door using your phone. It utilizes a Raspberry Pi 5 to control the lock.

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
│   ├── motor_controller.py  # Motor control functions (open, close, stop)
│   └── bluetooth_manager.py # Bluetooth connections and command parsing
├── fsm/
│   ├── __init__.py
│   ├── states.py            # System state enumerations
│   ├── transitions.py       # Transition conditions and triggers
│   └── state_machine.py     # FSM logic and state transitions
└── example_coffee_machine/   # Example reference implementation
```

## Hardware Requirements

- Raspberry Pi 5
- Motor controller (L298N or similar)
- DC Motor for lock mechanism
- Bluetooth module (for phone connectivity)

## Pin Configuration

Default pin assignments (configurable in `config/settings.py`):
- `MOTOR_PIN = 18`
- `IN1_PIN = 23`
- `IN2_PIN = 24`

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd smart-lock
```

2. Install required dependencies:
```bash
pip install RPi.GPIO pybluez
```

3. Configure settings in `config/settings.py` if needed.

## Usage

Coming soon...

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]

