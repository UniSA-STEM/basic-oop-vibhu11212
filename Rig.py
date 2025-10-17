"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Vibhu Karthikeya Pothanaboina
ID: 110446905
Username: potvy001
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name):
        self.name = name
        self.damage_couter = 0
        self.broken_state = False
        self.storage = [] # Starts with 2 Data spikes and 1 Removable Drive
        self.level = 0