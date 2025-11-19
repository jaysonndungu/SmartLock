#!/usr/bin/env python3
"""
Simple trigger script for SmartLock
Call this from RaspController/SSH to unlock the door.
The main file handles the unlock -> wait -> lock sequence.
"""

from main import unlock_door

if __name__ == "__main__":
    unlock_door()
