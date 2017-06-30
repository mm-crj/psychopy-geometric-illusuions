from PIL import Image, ImageDraw
from math import *
im = Image.new('L', (400, 400), (0, 0, 0)) 
draw = ImageDraw.Draw(im)

#starting point
x0=100.0
y0=200.0
#wing length
w=56.0
#Shaft length
s=176.0
th=radians(75)
x=int(round(cos(th)*w))
y=int(round(sin(th)*w))

#the shaft
draw.line((x0,y0,x0+s,y0), fill=0, width=3)
#the left wings
draw.line((x0,y0, x0+x, y0-y), fill=0, width=3)
draw.line((x0,y0, x0+x, y0+y), fill=0, width=3)
draw.line((x0,y0, x0-x, y0-y), fill=0, width=3)
draw.line((x0,y0, x0-x, y0+y), fill=0, width=3)

draw.line((x0+s,y0,x0+s-x, y0-y), fill=0, width=3)
draw.line((x0+s,y0, x0+s-x, y0+y), fill=0, width=3)
draw.line((x0+s,y0,x0+s+x, y0-y), fill=0, width=3)
draw.line((x0+s,y0, x0+s+x, y0+y), fill=0, width=3)

#im.save("ml_var_exp_75.png")
im.show()
