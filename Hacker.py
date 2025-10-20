"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Hacker:
    def __init__(self):
        self.__name = "Bitstar"
        self.__inventory = ["CryptoToken"]
        self.__rigs = None
        self.__trace_level = 0

        def get_name(self):
            return self.__name

        def get_inventory(self):
            return self.__inventory

        def get_rigs(self):
            return self.__rigs

        def set_rigs(self, rigs):
            self.__rigs = rigs

        def get_trace_level(self):
            return self.__trace_level

        def set_trace_level(self, trace_level):
            self.__trace_level = trace_level

        # properties for instance attributes
        name = property(get_name)
        inventory = property(get_inventory)
        rigs = property(get_rigs, set_rigs)
        trace_level = property(get_trace_level, set_trace_level)

        def aquire_a_rig(self, rig):
            pass

        def check_trace_threshold(self):
            pass

        def launch_data_spike(self, other_rig):
            pass

        def extract_assets(self, other_rig):
            pass

        def encrypt_assets(self):
            pass

        def decrypt_assets(self):
            pass

        def upgrade_rigs(self):
            pass

        def store_to_inventory(self):
            pass

        def retrieve_from_inventory(self):
            pass
