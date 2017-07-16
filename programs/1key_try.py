from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
from random import randint, shuffle
from psychopy.iohub import launchHubServer, EventConstants

# By default, ioHub will create Keyboard and Mouse devices and
# start monitoring for any events from these devices only.      
io=launchHubServer(psychopy_monitor_name='testMonitor')

#range of the reference line 
s=80.0

keyboard=io.devices.keyboard
increment = 0 # initial value of scaling factor

#value in the rating scale
rate1=rate=rate2=0.0

increment = 0.0 # initial value of scaling factor#range of the rating scale
range=10.0

win = visual.Window(
        size=[800, 800],
        units="pix",
        fullscr=0,
        color=[1, 1, 1],
        monitor="testMonitor",
        allowGUI=1,
        winType='pyglet'
        )

dev=randint(-s,s)
refline=visual.Line(win=win,start=(-99,-100),end=(77+dev,-100),lineColor='black',lineWidth=3)

ratingScale = visual.RatingScale(win=win, low=1, high=range ,pos=[0,-230],
        precision=10, scale='Length Scale', acceptText="Apply!!", showValue=0,
        lineColor="white", textColor="White", markerStart=(range-1.0)*(dev/(2.0*s)+0.5), 
        marker='circle', markerColor='grey', size=0.75)

while ratingScale.noResponse:
    rate=ratingScale.getRating() 
    ratingScale.draw()
    for event_io in keyboard.getEvents():
        if event_io.type == EventConstants.KEYBOARD_PRESS:
            print event_io.key
            if event_io.key == u'right':
                increment = 0.01 # move one step to the right
            elif event_io.key == u'left':
                increment = -0.01 # move one step to the left

        if event_io.type == EventConstants.KEYBOARD_RELEASE:
            increment = 0 # stop changing position

    
    ratingScale.markerPlacedAt += increment
    
    print ratingScale.markerPlacedAt,rate
    #ratingScale.markerPlaced = True 

    if  rate!=rate1:
            refline=visual.Line(win=win,start=(-99-((2.0*(rate-1.0)
                    /(range-1))-1)*(s/2.0),-100),end=(77+((2.0*(rate-1.0)
                    /(range-1))-1)*(s/2.0),-100
                    ),lineColor='black',lineWidth=3)
    refline.draw()
    
    win.flip()
    rate1=rate
# #for closing program with escape and q keys
#     while True: #continue until keypress
#     #handle key presses each frame
#         for key in event.getKeys():
#             if key in ['escape','q']:
#                 win.close()
#                 io.quit()
#                 core.quit()

win.close()
io.quit()
core.quit()
