"""
Hardware module for SmartLock system.
Contains motor control and Bluetooth communication functionality.
"""

from .motor_controller import MotorController
from .bluetooth_manager import BluetoothManager

__all__ = ['MotorController', 'BluetoothManager']

