"""
File: main.py
Description: <A brief description of this Python module.>
Author: <full name>
ID: <student_id>
Username: <username>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Rig import Rig
from Asset import Asset


def test_acquire_rig_and_upgrade():
    print("--- SCENARIO 1: ACQUIRE AND UPGRADE ---")
    hacker = Hacker("person1")
    rig = Rig("rig1")
    print(hacker)  # To see initial hacker information

    hacker.acquire_a_rig(rig)
    print(hacker)  # To see if hacker has acquired a rig

    hacker.upgrade_rigs()  # Upgrade Rig (requires a Hardware Patch)

    hacker.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs."))

    hacker.upgrade_rigs()
    print(hacker.rig)


test_acquire_rig_and_upgrade()
