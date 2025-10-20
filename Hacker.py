"""
File: Hacker.py
Description: <Hacker module represents a hacker class, who owns a rig and his attributes and methods are in this module
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig


class Hacker:
    """Represents a hacker who can acquire a rig, manage assets,and perform
     actions."""

    def __init__(self, name):
        """ Initialises a Hacker object. """
        self.__name = name
        self.__inventory = [Asset("CryptoToken",
                                  "Used to acquire or repair rigs")]
        self.__rig = None
        self.__trace_level = 0

    def get_name(self):
        """Returns the hacker's name."""
        return self.__name

    def get_inventory(self):
        """Returns the list of assets in the hacker's inventory."""
        return self.__inventory

    def get_rig(self):
        """Returns the hacker's active rig object, or None if there isn't one."""
        return self.__rig

    def set_rig(self, rig):
        """Assigns an active rig to the hacker."""
        self.__rig = rig

    def get_trace_level(self):
        """Returns the hacker's current trace level."""
        return self.__trace_level

    def set_trace_level(self, trace_level):
        """Sets the hacker's trace level."""
        self.__trace_level = trace_level

    # properties for instance attributes
    name = property(get_name)
    inventory = property(get_inventory)
    rig = property(get_rig, set_rig)
    trace_level = property(get_trace_level, set_trace_level)

    def acquire_a_rig(self, rig):
        """Acquires a rig for the hacker, consuming a CryptoToken."""
        # Checks for and consumes a "CryptoToken" from inventory
        if self.scan_and_remove_from_inventory("CryptoToken"):
            # Assigns the passed-in rig object to the hacker.
            self.rig = rig
            print(f"{self.name} has activated rig {self.rig.name}")
        else:
            print("No Crypto Tokens")

    def scan_and_remove_from_inventory(self, name):
        """Finds an asset by name in the inventory, removes it, and returns it."""
        # Loops through each asset object in the inventory list
        for asset in self.inventory:
            if asset.asset_name == name:
                # Removes the found asset from the inventory
                self.inventory.remove(asset)
                # Returns the asset object that was found and removed
                return asset
        return None

    def display_trace_warning(self):
        """Prints a warning message if the trace level is above the threshold"""
        # Checks if the trace level is over the limit
        if self.trace_level > 5:
            print(
                f"WARNING: {self.name} is exposed! Trace level is {self.trace_level}."
                f" Sensitive actions are now blocked. Please reduce your trace")

    def check_trace_threshold(self):
        """Checks if the trace level is over the safe threshold."""
        # Checks if the trace level is over the limit 5
        if self.trace_level > 5:
            # Prints a message and returns False.
            print(f"Trace level for {self.name} is too high! ")
            return False
        return True

    def launch_data_spike(self, other_rig):
        """Launches an attack on a target rig, consuming a Data Spike."""
        # Checks if trace level is safe and a rig is equipped
        if self.check_trace_threshold() and self.rig:
            # Tries to get a Data Spike from the rig's storage
            if self.rig.release_from_rig("Data Spike"):
                other_rig.take_hit()  # Target rig is got hit
                self.trace_level += 1  # Trace level increases by 1
                self.display_trace_warning()

    def extract_assets(self, other_rig):
        """Extracts all unencrypted assets from a broken rig, consuming a Removable Drive."""
        # Checks trace level and consumes a Removable Drive
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

    def encrypt_inventory_asset(self, asset_name):
        """Encrypts an asset in the hacker's inventory, consuming a Security Chip."""
        chip = self.scan_and_remove_from_inventory("Security Chip")
        if chip:  # cheks if security chip is in inventory
            for asset in self.inventory:  # searches asset by name
                if asset.asset_name == asset_name:
                    asset.encrypted = True
            self.inventory.append(chip)  # adds security chip back once used
            return "Encrypted"
        else:
            return "no security chip"

    def decrypt_inventory_asset(self, asset_name):
        """Decrypts an asset in the hacker's inventory,consuming a Security Chip"""
        chip = self.scan_and_remove_from_inventory("Security Chip")
        if chip:  # cheks if security chip is in inventory
            for asset in self.inventory:  # searches asset by name
                if asset.asset_name == asset_name:
                    asset.encrypted = False
            self.inventory.append(chip)  # adds security chip back once used
            return "Decrypted"
        else:
            return "no security chip"

    def encrypt_rig_asset(self, asset_name):
        """Encrypts an asset in the rig's storage, consuming a Security Chip."""
        if not self.rig:  # checks if rig exists
            return "no rig"
        else:
            chip = self.scan_and_remove_from_inventory("Security Chip")
            if chip:  # cheks if security chip is in inventory
                for asset in self.rig.storage:  # searches asset by name
                    if asset.asset_name == asset_name:
                        asset.encrypted = True
                self.inventory.append(chip)  # adds security chip back once used
                return "Encrypted"
            else:
                return "no security chip"

    def decrypt_rig_asset(self, asset_name):
        """Decrypts an asset in the rig's storage, consuming a Security Chip"""
        if not self.rig:  # checks if rig exists
            return "no rig"
        else:
            chip = self.scan_and_remove_from_inventory("Security Chip")
            if chip:  # cheks if security chip is in inventory
                for asset in self.rig.storage:  # searches asset by name
                    if asset.asset_name == asset_name:
                        asset.encrypted = False
                self.inventory.append(chip)  # adds security chip back once used
                return "Decrypted"
            else:
                return "no security chip"

    def upgrade_rigs(self):
        """Upgrades the active rig, consuming a Hardware Patch."""
        # if statement checks is trace level is normal
        if self.check_trace_threshold():
            if self.rig and self.scan_and_remove_from_inventory(
                    "Hardware Patch"):
                self.rig.upgrade()  # upgrades rig if hardware patch exists
                self.trace_level += 1
                self.display_trace_warning()
            else:
                print("No Hardware Patch, Unable to update")
        else:
            print("Trace too high cannot upgrade")

    def repair_rig(self):
        """Repairs the rig by consuming a CryptoToken"""
        # if statement checks if hacker has a CryptoToken
        if self.scan_and_remove_from_inventory("CryptoToken"):
            if self.rig:
                self.rig.repair()  # calls repair method from Rig module
        else:
            print(f"{self.name} has no CryptoToken to perform repairs.")

    def move_to_rig(self, name):
        """Moves an asset from the hacker's inventory to the rig's storage"""
        if self.rig:  # if statement to check rig exists for hacker
            asset_to_move = self.scan_and_remove_from_inventory(name)
            if asset_to_move:  # checks if inventory has asset
                self.rig.store_to_rig(asset_to_move)  # adds asset to rig
                print(f"Moved '{name}' to {self.rig.name}.")

    def retrieve_from_rig(self, name):
        """Moves an asset from the rig's storage to the hacker's inventory"""
        if self.rig:  # if statement to check rig exists for hacker
            asset_to_retrieve = self.rig.release_from_rig(name)
            if asset_to_retrieve:  # checks if released from rig
                self.inventory.append(
                    asset_to_retrieve)  # adds asset to inventor
                print(f"Retrieved '{name}' from {self.rig.name}.")

    def __str__(self):
        rig_name = self.rig.name if self.rig else "None"
        if not self.inventory:
            inventory_str = "Empty"
        else:
            inventory_str = ""
            for asset in self.inventory:
                inventory_str += asset.asset_name + ", "
        return (f"--- HACKER ---\n"
                f"Name: {self.name}\n"
                f"Trace Level: {self.trace_level}\n"
                f"Rig Equiped: {rig_name}\n"
                f"Inventory: {inventory_str}\n")
