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

        def aquire_a_rig(self, rig): # DONE
            if self.scan_and_remove_from_inventory("CryptoToken"):
                self.rig = rig
                print(f"{self.name} has activated rig {self.rig.name}")
            else:
                print("No Crypto Tokens")

        def scan_and_remove_from_inventory(self, name): #DONE
            for asset in self.inventory:
                if asset.asset_name == name:
                    self.inventory.remove(asset)
                    return asset
            return None

        def check_trace_threshold(self):

        def launch_data_spike(self, other_rig):

        def extract_assets(self, other_rig):

        def encrypt_assets(self):

        def decrypt_assets(self):
            pass

        def upgrade_rigs(self):
            pass

        def move_to_rig(self, name):  # DONE
            if self.rig:
                asset_to_move = self.scan_and_remove_from_inventory(name)
                if asset_to_move:
                    self.rig.store_to_rig(asset_to_move)
                    print(f"Moved '{name}' to {self.rig.name}.")

        def retrieve_from_rig(self, name): #DONE
            if self.rig:
                asset_to_retrieve = self.rig.release_from_rig(name)
                if asset_to_retrieve:
                    self.inventory.append(asset_to_retrieve)
                    print(f"Retrieved '{name}' from {self.rig.name}.")
