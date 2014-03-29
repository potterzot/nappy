"""Enhancements and other things having to do with data types."""

class AutoVivification(dict):
    """Implements perl's autovivification feature. Calling a dictionary via keys
    will automatically create those keys if they don't exists."""
    
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
            
        except KeyError:
            value = self[item] = type(self)()
            return value
