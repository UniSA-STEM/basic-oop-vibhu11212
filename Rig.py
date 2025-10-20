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
    def __init__(self, name):
        self.__name = name
        self.__damage_couter = 0
        self.__broken_state = False
        self.__storage = [Asset("Data Spike", "Used in batles"),
                          Asset("Data Spike", "Used in batles"),
                          Asset("Removable Drive", "Found in rigs and used for "
                                                   "extracton")]
        self.__storage_capacity = 6
        self.__level = 0

    def get_name(self):
        return self.__name

    def get_damage_counter(self):
        return self.__damage_couter

    def get_broken_state(self):
        return self.__broken_state

    def set_damage_counter(self, counter):
        self.__damage_couter = counter

    def set_broken_state(self, state):
        self.__broken_state = state

    def get_storage(self):
        return self.__storage

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def get_storage_capacity(self):
        return self.__storage_capacity

    def set_storage_capacity(self, value):
        self.__storage_capacity = value

    # properties for instance attributed
    name = property(get_name)
    damage_counter = property(get_damage_counter, set_damage_counter)
    broken_state = property(get_broken_state, set_broken_state)
    storage = property(get_storage)
    level = property(get_level, set_level)
    storage_capacity = property(get_storage_capacity, set_storage_capacity)

    def repair(self):
        if self.damage_counter > 0:
            self.damage_counter = 0
            self.broken_state = False
            print(f"{self.name} has been repaired.")
        else:
            print(f"{self.name} does not require any repairs.")

    def upgrade(self):
        self.level += 1
        self.storage_capacity += 2
        print(
            f"{self.name} upgraded to Level {self.level} with storage capacity {self.storage_capacity}.")

    def take_hit(self):
        damage_threshold = 2 + self.level
        self.damage_counter += 1
        if self.damage_counter >= damage_threshold:
            self.broken_state = True

    def generate_asset(self):
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

    def store_to_rig(self, asset):  # DONE
        if len(self.storage) < self.storage_capacity:
            self.storage.append(asset)
        else:
            print(
                f"Storage full on {self.name}. Cannot store {asset.asset_name}")

    def release_from_rig(self, name):  # DONE
        for asset in self.storage:
            if asset.asset_name == name and not asset.encrypted:
                self.storage.remove(asset)
                return asset
        return None

    def get_condition(self):
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
