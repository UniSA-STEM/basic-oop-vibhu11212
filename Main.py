"""
File: main.py
Description: This module has testable code, imports classes from other
modules and tests them here
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Rig import Rig
from Asset import Asset


def test_acquire_rig_and_upgrade():
    print("--- SCENARIO : ACQUIRE AND UPGRADE ---")
    hacker = Hacker("person1")
    rig = Rig("rig1")
    print(hacker)  # To see initial hacker information

    hacker.acquire_a_rig(rig)
    print(hacker)  # To see if hacker has acquired a rig

    hacker.upgrade_rigs()  # Upgrade Rig (requires a Hardware Patch)

    hacker.inventory.append(Asset("Hardware Patch", "Used to upgrade rigs."))

    hacker.upgrade_rigs()
    print(hacker.rig)


def test_battle_and_extraction():
    print("\n--- SCENARIO 2: BATTLE AND EXTRACTION ---")
    # Setup two hackers and two rigs
    attacker = Hacker("P1")
    defender = Hacker("P2")
    rig_p1 = Rig("R1")
    rig_p2 = Rig("r2")

    # Both hackers acquire their rigs
    attacker.acquire_a_rig(rig_p1)
    defender.acquire_a_rig(rig_p2)
    rig_p2.get_condition()

    # Attacker launches data spikes until the defender's rig is broken

    attacker.launch_data_spike(rig_p2)
    attacker.launch_data_spike(rig_p2)
    print(rig_p2.get_condition())

    # Add a Removable Drive to the attacker's inventory to perform the action
    attacker.inventory.append(Asset("Removable Drive", "Used for extraction"))
    attacker.extract_assets(rig_p2)

    print(attacker)  # Shows the attacker's new inventory


def test_encryption_and_transfer():
    print("\n--- SCENARIO 3: ENCRYPTION AND TRANSFER ---")
    hacker = Hacker("p1")
    rig = Rig("r1")
    hacker.acquire_a_rig(rig)
    hacker.inventory.append(Asset("Security Chip", "Used to encrypt assets"))
    print(rig)
    hacker.encrypt_rig_asset("Data Spike")
    print(rig)
    rig.con
    hacker.retrieve_from_rig("Data Spike")

    print(hacker)


test_acquire_rig_and_upgrade()
print()
print("Next test")
test_battle_and_extraction()
# test_encryption_and_transfer()
