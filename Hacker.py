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

    def aquire_a_rig(self, rig):  # DONE
        if self.scan_and_remove_from_inventory("CryptoToken"):
            self.rig = rig
            print(f"{self.name} has activated rig {self.rig.name}")
        else:
            print("No Crypto Tokens")

    def scan_and_remove_from_inventory(self, name):  # DONE
        for asset in self.inventory:
            if asset.asset_name == name:
                self.inventory.remove(asset)
                return asset
        return None

    def display_trace_warning(self):

        if self.trace_level > 5:
            print(
                f"WARNING: {self.name} is exposed! Trace level is {self.trace_level}."
                f" Risky actions are now blocked.")

    def check_trace_threshold(self):
        if self.trace_level > 5:
            print(f"Trace level for {self.name} is too high! ")
            return False
        return True

    def launch_data_spike(self, other_rig):
        if self.check_trace_threshold() and self.rig:
            if self.rig.release_from_rig("Data Spike"):
                other_rig.take_hit()
                self.trace_level += 1
                self.display_trace_warning()

    def extract_assets(self, other_rig):
        if self.check_trace_threshold() and self.scan_and_remove_from_inventory(
                "Removable Drive"):
            if other_rig.broken_state:
                assets_to_extract = [asset for asset in
                                     other_rig.storage if
                                     not asset.encrypted]
                for asset in assets_to_extract:
                    extracted = other_rig.release_from_rig(
                        asset.asset_name)
                    if extracted:
                        self.inventory.append(extracted)
                self.trace_level += 1
                self.display_trace_warning()

    def encrypt_inventory_asset(self, asset_name):  # encrypt in inventory
        chip = self.scan_and_remove_from_inventory("Security Chip")
        if chip:
            for asset in self.inventory:
                if asset.asset_name == asset_name:
                    asset.encrypted = True
                    return "Encrypted"
            self.inventory.append(chip)
        else:
            return "no security chip"

    def decrypt_inventory_asset(self, asset_name):  # decryppt in inventory
        chip = self.scan_and_remove_from_inventory("Security Chip")
        if chip:
            for asset in self.inventory:
                if asset.asset_name == asset_name:
                    asset.encrypted = False
                    return "Decrypted"
            self.inventory.append(chip)
        else:
            return "no security chip"

    def encrypt_rig_asset(self, asset_name):  # encrypt in rig storage
        if not self.rig:
            return "no rig"
        else:
            chip = self.scan_and_remove_from_inventory("Security Chip")
            if chip:
                for asset in self.rig.storage:
                    if asset.asset_name == asset_name:
                        asset.encrypted = True
                        return "Encrypted"
                self.inventory.append(chip)
            else:
                return "no security chip"

    def decrypt_rig_asset(self, asset_name):  # decrypt in rig storage
        if not self.rig:
            return "no rig"
        else:
            chip = self.scan_and_remove_from_inventory("Security Chip")
            if chip:
                for asset in self.rig.storage:
                    if asset.asset_name == asset_name:
                        asset.encrypted = False
                        return "Decrypted"
                self.inventory.append(chip)
            else:
                return "no security chip"

    def upgrade_rigs(self):
        if self.check_trace_threshold():
            if self.rig and self.scan_and_remove_from_inventory(
                    "Hardware Patch"):
                self.rig.upgrade()
                self.trace_level += 1
                self.display_trace_warning()

    def repair_rig(self):
        if self.scan_and_remove_from_inventory("CryptoToken"):
            if self.rig:
                self.rig.repair()
        else:
            print(f"{self.name} has no CryptoToken to perform repairs.")

    def move_to_rig(self, name):  # DONE
        if self.rig:
            asset_to_move = self.scan_and_remove_from_inventory(name)
            if asset_to_move:
                self.rig.store_to_rig(asset_to_move)
                print(f"Moved '{name}' to {self.rig.name}.")

    def retrieve_from_rig(self, name):  # DONE
        if self.rig:
            asset_to_retrieve = self.rig.release_from_rig(name)
            if asset_to_retrieve:
                self.inventory.append(asset_to_retrieve)
                print(f"Retrieved '{name}' from {self.rig.name}.")
