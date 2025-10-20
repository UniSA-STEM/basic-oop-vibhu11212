"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random


class Rig:
    """Represents a hacker's computer rig, which can be upgraded, take damage, and store assets"""

    def __init__(self, name):
        """Initialises a Rig object"""
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = [Asset("Data Spike", "Used in battles"),
                          Asset("Data Spike", "Used in battles"),
                          Asset("Removable Drive", "Found in rigs and used for "
                                                   "extraction")]
        self.__storage_capacity = 6
        self.__level = 0

    def get_name(self):
        """Returns the rig's name"""
        return self.__name

    def get_damage_counter(self):
        """Returns the current damage counter"""
        return self.__damage_counter

    def get_broken_state(self):
        """Returns the rig's broken state (True or False)"""
        return self.__broken_state

    def set_damage_counter(self, counter):
        """Sets the rig's damage counter"""
        self.__damage_counter = counter

    def set_broken_state(self, state):
        """Sets the rig's broken state"""
        self.__broken_state = state

    def get_storage(self):
        """Returns the list of assets in the rig's storage"""
        return self.__storage

    def get_level(self):
        """Returns the rig's current upgrade level"""
        return self.__level

    def set_level(self, level):
        """Sets the rig's upgrade level"""
        self.__level = level

    def get_storage_capacity(self):
        """Returns the rig's maximum storage capacity"""
        return self.__storage_capacity

    def set_storage_capacity(self, value):
        """Sets the rig's maximum storage capacity"""
        self.__storage_capacity = value

    # properties for instance attributed
    name = property(get_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    broken_state = property(get_broken_state, set_broken_state)
    storage = property(get_storage)
    level = property(get_level, set_level)
    storage_capacity = property(get_storage_capacity, set_storage_capacity)

    def repair(self):
        """Repairs the rig if it is damaged by resetting its state"""
        if self.damage_counter > 0:
            self.damage_counter = 0
            self.broken_state = False
            print(f"{self.name} has been repaired.")
        else:
            print(f"{self.name} does not require any repairs.")

    def upgrade(self):
        """Increases the rig's level and storage capacity"""
        self.level += 1
        self.storage_capacity += 2
        print(
            f"{self.name} upgraded to Level {self.level} with storage capacity {self.storage_capacity}.")

    def take_hit(self):
        """Increases the rig's damage counter by one and checks if it has become broken"""
        damage_threshold = 2 + self.level
        self.damage_counter += 1
        if self.damage_counter >= damage_threshold:
            self.broken_state = True

    def generate_asset(self):
        """Generates a random asset and adds it to storage if there is capacity"""
        possible_assets = [
            Asset("CryptoToken", "Used to acquire or repair rigs"),
            Asset("Data Spike", "Used in battles"),
            Asset("Removable Drive", "Found in rigs and used for "
                                     "extraction"),
            Asset("Security Chip", "Used to encrypt or decrypt assets"),
            Asset("Hardware Patch", "Used to upgrade rigs")
        ]
        new_asset = random.choice(possible_assets)
        if len(self.storage) < self.storage_capacity:
            self.storage.append(new_asset)

    def store_to_rig(self, asset):
        """Stores a given asset object in the rig's storage if there is capacity""""
        if len(self.storage) < self.storage_capacity:
            self.storage.append(asset)
        else:
            print(
                f"Storage full on {self.name}. Cannot store {asset.asset_name}")

    def release_from_rig(self, name):
        """Finds an asset by name, removes it from storage, and returns it if not encrypted"""
        for asset in self.storage:
            if asset.asset_name == name and not asset.encrypted:
                self.storage.remove(asset)
                return asset
        return None

    def get_condition(self):
        """Returns a string about the rig's current condition, level,
        and damage"""
        damage_threshold = 2 + self.level
        damage_info = f"[Hits Take:{self.damage_counter}/Max Limit:{damage_threshold}]"
        if self.broken_state:
            status = "Broken"
        else:
            condition_names = ["Novice", "Silver", "Pristine", "Gold",
                               "Platinum", "Diamond"]  # Level 0 to 5

            if 0 <= self.level < len(condition_names):
                status = condition_names[self.level]
            else:
                status = "Advanced"
        return f"{status} (Level {self.level} Damage info: {damage_info})"

    def __str__(self):
        if not self.storage:
            stored_items_str = "Empty"
        else:
            stored_items_str = ""
            for asset in self.storage:
                stored_items_str += asset.asset_name + ", "
        return (f"--- RIG ---\n"
                f"Name: {self.name}\n"
                f"Condition: {self.get_condition()}\n"
                f"Stored Assets: {stored_items_str}\n")
