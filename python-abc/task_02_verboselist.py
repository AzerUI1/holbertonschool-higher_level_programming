#!/usr/bin/python3
from abc import ABC, abstractmethod


class VerboseList(list):

    def append(self, value):
        print(f"Added [{value}] to the list.")
        super().append(value)

    def extend(self, value):
        print(f"Extended the list with [{len(value)}] items.")
        super().extend(value)

    def remove(self, value):

        # Checking if item is in list
        if value in self:
            print(f"Removed [{value}] from the list.")
        super().remove(value)

    def pop(self, value=None):

        # Checking if index is specified
        if value is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
            return item
        else:
            item = super().pop(value)
            print(f"Popped [{item}] from the list.")
            return item
