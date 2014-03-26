"""
Methods for handling web-based things.
"""

from urllib.request import urlretrieve


def get_file(url, saveto=False):
    """Pulls the file and saves to the local drive, optionally with 
    the name specified by saveto."""
    request = urlretrieve(url, saveto)
    



