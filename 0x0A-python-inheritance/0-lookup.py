ble File  9 lines (7 sloc)  232 Bytes

#!/usr/bin/python3
# 0-lookup.py
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
