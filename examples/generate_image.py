import random
import numpy as np
from nappy.image import IntegerImage
from PIL import Image

def redfn(p):
    q = p['params']
    color = 255 - (q['1'] * np.sqrt((q['2']-p['i'])**2 + (q['3']-p['j'])**2)) / \
        (q['6'] * np.sqrt(abs(np.sin(q['7'] * ((q['4']-p['i'])**2 + (q['5']-p['j'])**2)))+1))
    return int(color)

def greenfn(p):
    q = p['params']
    color = 255 - (q['1'] * np.sqrt((q['2']-p['i'])**2 + (q['3']-p['j'])**2))/ \
        (q['6'] * np.sqrt(abs(np.tan(q['7'] * ((q['4']-p['i'])**2 + (q['5']-p['j'])**2)))+1))
    return int(color)

def bluefn(p):
    q = p['params']
    #color = (q['1'] * np.sqrt((q['2']-p['i'])**2 + (q['3']-p['j'])**2))/ \
    color = 255 - (q['1'] * np.sqrt((q['2']-p['i'])**2 + (q['3']-p['j'])**2))/ \
        (q['6'] * np.sqrt(abs(np.tan(q['7'] * ((q['4']-p['i'])**2 + (q['5']-p['j'])**2))**2)+.01))
    return int(color)

# width and height
x=1500
y=500

rgb={} 
gbr={} 
brg={}
rgb['1'] = random.uniform(.1,.5) #Amount of color
gbr['1'] = random.uniform(.25,1) # amount of color
brg['1'] = random.uniform(.01,.5) # amount of color
rgb['6'] = 1 #random.randint(50,200) # size of sphere
gbr['6'] = 1 #random.uniform(1,10) # size of sphere
brg['6'] = 1 #random.randint(40,400) # number of rings. Higher is less rings
rgb['7'] = random.uniform(.000001, 200) # distance of ripples
gbr['7'] = random.uniform(20,100) # pattern decay. higher means less decay
brg['7'] = random.uniform(.0000001,.00001) # distance of ripples

for p in ['2', '4']:
    # Controls the x location of the element
    rgb[p] = random.uniform(-.1*x,1.1*x)
    gbr[p] = random.uniform(-.1*x,1.1*x)
    brg[p] = random.uniform(-.1*x,1.1*x)
for p in ['3', '5']:
    # Controls the y location of the element
    rgb[p] = random.uniform(-.1*y,1.1*y)
    gbr[p] = random.uniform(-.1*y,1.1*y)
    brg[p] = random.uniform(-.1*y,1.1*y)

img = IntegerImage('test.png', redfn, greenfn, bluefn, x, y)

img.draw(p_red=rgb, p_green=gbr, p_blue=brg)

# add a mask for the logo
img.save()





