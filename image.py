from PIL import Image, ImageDraw, ImageFont
from math import *
import random


"""
first two numbers are x and y of a sphere
third number is 
fourth and fifth numbers are x and y of ripples
6th is amplitude of ripples
last number - scales the amount of color
"""


def set_blue(i,j,x,y,p1=20055,p2=100,p3=150,p4=30,p5=45,p6=10,p7=.1):
    """Algorithm to create the blue portion of the pixel color."""
    #color = 255/(sqrt((30  -i)**2 + (112  -j)**2)+1)/(sqrt(abs(sin((sqrt((100-i)**2 + (100 -j)**2))/75)))+1)/.01
    #color = p1/(sqrt((p2-i)**2 + (p3-j)**2)+1)/(sqrt(abs((sqrt((p4-i)**2 + (p5-j)**2))/p6))+1)/p7
    color = p1/(sqrt((p2-i)**2 + (p3-j)**2)+1)/(sqrt(abs((sqrt((p4-i)**2 + (p5-j)**2)))+1)/p6)
    return int(color)

def set_green(i,j,x,y,p1=4000,p2=100,p3=150,p4=10,p5=300, p6=50,p7=.5):
    """Algorithm to create the green portion of the pixel color."""
    color = p1/(sqrt((p2-i)**2 + (p3-j)**2)+1)/(sqrt(abs(1+sin((p4-i)**2 + (p5-j)**2)**2)+1)/p6)/p7
    return int(color)+random.randint(-1,1)

def set_red(i,j,x,y,p1=8000,p2=100,p3=150,p4=10,p5=300,p6=25,p7=.3):
    """Algorithm to create the red portion of the pixel color. """
    #color = (sqrt((10 -i)**2 + (100 -j)**2)+1)/(sqrt(abs(sin((sqrt((6 -i)**2 + (8  -j)**2))/15)))+1)/.25
    color = p1/(sqrt((p2-i)**2 + (p3-j)**2)+1)/(sqrt(abs(sin((sqrt((p4-i)**2 + (p5-j)**2))/p6)))+1)/p7
    return int(color)

def make_image(red, green, blue, x=1600, y=2400):
    """Create the image associated with this subject."""
    img = Image.new('RGB', (x,y), 'white')
    draw = ImageDraw.Draw(img)
  
    rgb={} 
    gbr={} 
    brg={}
    rgb['p1'] = random.randint(500,5000)
    gbr['p1'] = random.randint(500,25000)
    brg['p1'] = random.randint(500,25000)
    rgb['p6'] = random.randint(3,20)
    gbr['p6'] = random.uniform(.5,1)
    brg['p6'] = random.randint(5,25)
    rgb['p7'] = random.uniform(.1,.3)
    gbr['p7'] = random.uniform(.5,1)
    brg['p7'] = random.uniform(.01,.3)
    
    for p in ['p2', 'p4']:
        rgb[p] = random.randint(0,x)
        gbr[p] = random.randint(0,x)
        brg[p] = random.randint(0,x)
    for p in ['p3', 'p5']:
        rgb[p] = random.randint(0,y)
        gbr[p] = random.randint(0,y)
        brg[p] = random.randint(0,y)
    

    for i in range(x):
        for j in range(y):
            r =   red(i,j,x,y,rgb['p1'], rgb['p2'], rgb['p3'], rgb['p4'], rgb['p5'], rgb['p6'], rgb['p7'])
            g = green(i,j,x,y,gbr['p1'], gbr['p2'], gbr['p3'], gbr['p4'], gbr['p5'], gbr['p6'], gbr['p7'])
            b =  blue(i,j,x,y,brg['p1'], brg['p2'], brg['p3'], brg['p4'], brg['p5'], brg['p6'], brg['p7'])
            d = (r,g,b)
            draw.point((i,j), d)

    ### Add the colors

    '''
    ### Add the DNA code text
    
    # Left side text
    draw.text((-4, 11), text1, fill='#333333', font=font)
    draw.text((-5, 10), text1, fill='white', font=font)
    
    # Right side text
    draw.text((int(x*1/3), int(y*.70)), text2, fill='black', font=font)
   
    # Add Title


    # Add Author Bar
    draw.rectangle((0,y,x,y*.8), fill='#1CD7DC', outline=None)     
    '''

    # Save the file
    #img.save('cover.png')
    img.show()
    #img.save()



def main():
    """"""
    make_image(set_red, set_green, set_blue, x=200, y=300)


main()
