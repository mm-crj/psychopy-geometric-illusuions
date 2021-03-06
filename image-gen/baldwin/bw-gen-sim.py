from PIL import Image, ImageDraw
from math import *
im = Image.new('L', (500, 500), (0, 0, 0)) 
draw = ImageDraw.Draw(im)

#starting point
x0=250.0
y0=150.0
y1=y0+200
#Shaft length
s=50.0

#wing length
w=1/3.5*s
#th=radians(75)
#x=int(round(cos(th)*w))
#y=int(round(sin(th)*w))

#the shaft
draw.line((x0-s/2,y0,x0+s/2,y0), fill=0, width=3)

#the left box
draw.line((x0-s/2,y0-w/2,x0-s/2,y0+w/2), fill=0, width=3)
draw.line((x0-s/2,y0-w/2,(x0-s/2-w),y0-w/2), fill=0, width=3)
draw.line((x0-s/2,y0+w/2,(x0-s/2-w),y0+w/2), fill=0, width=3)
draw.line(((x0-s/2-w),y0-w/2,(x0-s/2-w),y0+w/2), fill=0, width=3)

#right box
draw.line((x0+s/2,y0-w/2,x0+s/2,y0+w/2), fill=0, width=3)
draw.line((x0+s/2,y0-w/2,(x0+s/2+w),y0-w/2), fill=0, width=3)
draw.line((x0+s/2,y0+w/2,(x0+s/2+w),y0+w/2), fill=0, width=3)
draw.line(((x0+s/2+w),y0-w/2,(x0+s/2+w),y0+w/2), fill=0, width=3)

#control line
draw.line((x0-s/2,y1,x0+s/2,y1), fill=0, width=3)

im.save("bw_sim_s1-3.5.png")
im.show()
