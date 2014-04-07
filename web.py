"""
Methods for handling web-based things.
"""

from urllib.request import urlretrieve


def get_file(url, saveto=False, verbose=False):
    """Pulls the file and saves to the local drive, optionally with 
    the name specified by saveto."""
    
    def _verbose(blk, blk_size, size):
        """Handles the printing of the progress."""
        print(str(round(100*blk*blk_size/size))+ "% done...")
    
    if verbose: verbose=_verbose
    
    print("Downloading file: "+url)
    if saveto: print("... as "+saveto)

    urlretrieve(url, saveto, _verbose)
    



