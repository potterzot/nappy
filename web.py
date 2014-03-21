"""
Methods for handling web-based things.
"""

from url.request import urlretrieve


get_file(url, saveto=False):
    """Pulls the file and saves to the local drive, optionally with 
    the name specified by saveto."""
    request = urlretrieve(url, saveto)
    



