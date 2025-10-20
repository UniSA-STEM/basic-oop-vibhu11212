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

        # properties for instance attributed
        name = property(get_name)
        damage_counter = property(get_damage_counter, set_damage_counter)
        broken_state = property(get_broken_state, set_broken_state)
        storage = property(get_storage)
        level = property(get_level, set_level)

        def repair(self):
            if self.damage_counter > 0:
                self.damage_counter = 0
                self.broken_state = False
                print(f"{self.name} has been repaired.")
            else:
                print(f"{self.name} does not require any repairs.")

        def upgrade(self):
            self.level += 1

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
            self.__storage.append(new_asset)

        def store_to_rig(self, asset):  # DONE
            self.storage.append(asset)

        def release_from_rig(self, name):  # DONE
            for asset in self.storage:
                if asset.asset_name == name and not asset.encrypted:
                    self.storage.remove(asset)
                    return asset
            return None

        def rig_condition(self):
            if not self.broken_state:
                return f"Broken (Level {self.level})"

            condition_names = ["Novice", "Silver", "Pristine", "Gold",
                               "Platinum", "Diamond"]  # Level 0 to 5

            if 0 <= self.level < len(condition_names):
                status = condition_names[self.level]
            else:
                status = "Advanced"
            return f"{status} (Level {self.level})"

        def __str__(self):
            pass
