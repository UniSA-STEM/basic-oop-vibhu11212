"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset


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
            self.__name

        def get_damage_counter(self):
            self.__damage_couter

        def get_broken_state(self):
            self.__broken_state

        def set_broken_state(self, state):
            self.__broken_state = state

        def get_storage(self):
            self.__storage

        def get_level(self):
            self.__level

        def repair(self):
            pass

        def upgrade(self):
            pass

        def take_hit():
            pass

        def generate_asset(self):
            pass

        def store_to_rig(self):
            pass

        def release_from_rig(self):
            pass

        def rig_condition(self):
            # based on damage and upgrade level
            pass

        def __str__(self):
            pass
