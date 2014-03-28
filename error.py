"""
Custom error classes for use in various things.
"""

class UnmatchedHeadersError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
