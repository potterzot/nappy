"""
Methods for handling web-based things.
"""

from urllib.parse import quote_plus
from urllib.request import urlretrieve

def get(url, saveto=False, verbose=False):
    """Provides a get function to work with GET to fetch a file or via api."""
    
    def _verbose(blk, blk_size, size):
        """Handles the printing of the progress."""
        print(str(round(100*blk*blk_size/size))+ "% done...")
    
    if verbose: verbose=_verbose
    
    print("Downloading file: "+url)
    if saveto: print("... as "+saveto)
    
    urlretrieve(url, saveto, verbose)


def get_file(url, saveto=False, verbose=False):
    """Pulls the file and saves to the local drive, optionally with 
    the name specified by saveto."""
    get(url, saveto, verbose) 
    
def get_api(base, var_str, saveto=False, verbose=False):
    """Generic api call using a base url and variable string."""
    
    urlretrieve(url, saveto, _verbose)




def api_nass(var_dict, saveto=False, verbose=False, format="JSON"):
    """NASS quickstats API call"""
    # Base variables
    base="http://quickstats.nass.usda.gov/api/api_GET/?"
    config={'key':"2E499453-ED16-3FAF-BE39-6357DB38AEB9"
        , 'format': format}

    # We need an ordered list with key first and format last, as follows
    var_list = ['key']
    [var_list.append(key) for key in var_dict.keys()]
    var_list.append('format')

    # Then we convert to a url string
    var_str = "&".join( [item+'='+quote_plus(dict(config, **var_dict)[item]) for item in var_list] ) 
    url = base+var_str
       
    # Fetch the file
    get(url, saveto, verbose)

    
    


