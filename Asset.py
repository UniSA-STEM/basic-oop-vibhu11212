"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def get_asset_name(self):
        return self.__name

    def get_asset_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

    def set_encrypted(self, encrypted):
        self.__encrypted = encrypted

    def __str__(self):
        return f"{self.__name}: {self.__description} [{self.__encrypted}]" \
            if self.get_encrypted() else f"{self.__name}: {self.__description}"
