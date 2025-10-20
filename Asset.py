"""
File: Asset.py
Description: Asset module contains class asset to instantiate asset object
which is used in rigs and used by hacker
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    """Represents a digital asset with a name, description, and encryption status"""

    def __init__(self, name, description):
        """Initialises an Asset object"""
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_asset_name(self):
        """Returns the asset's name"""
        return self.__name

    def get_asset_description(self):
        """Returns the asset's description"""
        return self.__description

    def get_encrypted(self):
        """Returns the asset's encryption status (True or False)"""
        return self.__encrypted

    def set_encrypted(self, encrypted):
        """Sets the encryption status of the asset"""
        self.__encrypted = encrypted

    # properties for instance attributes
    asset_name = property(get_asset_name)
    asset_description = property(get_asset_description)
    encrypted = property(get_encrypted, set_encrypted)

    def __str__(self):
        encrypted_status = " [Encrypted]" if self.encrypted else ""
        return f"{self.asset_name}: {self.asset_description}{encrypted_status}"
