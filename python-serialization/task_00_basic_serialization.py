#!/usr/bin/env python3
"""Basic JSON serialization and deserialization"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save to JSON file"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize JSON file back into a Python dictionary"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
