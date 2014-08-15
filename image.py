"""
IntegerImage is a class that creates images based on the i and j pixel coordinates and a red, green, and blue function.
"""

class IntegerImage(object):
    """
    Builds an image based on 3 functions for different colors of a pixel and the i,j coordinate of that pixel. 

    Requires 3 functions, one for each of red, green, and blue. Each function must take parameters i,j,x,y, and any additional parameters that you pass through the classes 'draw' method.
    """

    def __init__(self, filename, redfn, greenfn, bluefn, x, y):
        """Create a new image."""
        from PIL import Image, ImageDraw
  
        self.filename = filename
        self.red = redfn 
        self.green = greenfn 
        self.blue = bluefn 
        self.x = x
        self.y = y
        self.Image = Image.new('RGB', (x,y), 'white')
        self.ImageDraw = ImageDraw.Draw(self.Image)

    def draw(self, p_red=None, p_green=None, p_blue=None):
        """Draw the image."""
        pen = self.ImageDraw
        params_red = {}



        for i in range(self.x):
            for j in range(self.y):
                r =   self.red({'i':i,'j':j,'x':self.x,'y':self.y,'params':p_red})
                g =   self.green({'i':i,'j':j,'x':self.x,'y':self.y,'params':p_green})
                b =   self.blue({'i':i,'j':j,'x':self.x,'y':self.y,'params':p_blue})
                pen.point((i,j), (r,g,b))

    def show(self):
        """Show the image."""
        self.Image.show

    def save(self):
        """Save the image to a file."""
        self.Image.save(self.filename)




