from PIL import Image, ImageDraw
from math import *
im = Image.new('L', (400, 400), (0, 0, 0)) 
draw = ImageDraw.Draw(im)

#starting point
x0=100.0
y0=120.0
#wing length
w=56.0
#Shaft length
s=176.0

#normal line
d=165.0

th=radians(165)
x=int(round(cos(th)*w))
y=int(round(sin(th)*w))

#the shaft
draw.line((x0,y0,x0+s,y0), fill=0, width=3)
#the left wings
draw.line((x0,y0, x0+x, y0-y), fill=0, width=3)
draw.line((x0,y0, x0+x, y0+y), fill=0, width=3)
draw.line((x0+s,y0,x0+s-x, y0-y), fill=0, width=3)
draw.line((x0+s,y0, x0+s-x, y0+y), fill=0, width=3)

#normal line
draw.line((x0,y0+d,x0+s,y0+d), fill=0, width=3)
im.save("ml_sim_165.png")
im.show()
