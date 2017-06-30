import os
import time
from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
from random import randint, shuffle
#from numpy import random



#user values
#image location
#im= '../images/ml/tests/exp/ml_exp_15.png'

#range of the reference line 
s=80.0

#value in the rating scale
rate1=rate=0.0

#range of the rating scale
range=10.0

#images location 
loc="../images/ml/tests/exp/"

#list of images
files= os.listdir(loc)
shuffle(files)

try:#try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:#if not there then use a default set
    expInfo = {
    'subject':'jwp',
    'gender':'M', 
    'age':0,
    'hand_pref':'R'
    }

dateStr=time.strftime("%d-%m-%Y-%R-%s")
#present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='Psychophysical Experiments', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)#save params to file for next time
else:
	pass

#make a text file to save data
fileName = expInfo['subject'] +'-'+loc.replace("/","-").rstrip(".")
file = open(fileName+'.csv', 'a')#append mode

file.write("%s,%s,%s,%s,%s\n" %(expInfo['subject'],expInfo['gender'],expInfo['age'],
	expInfo['hand_pref'],dateStr))

win = visual.Window(
	    size=[800, 800],
	    units="pix",
	    fullscr=1,
	    color=[1, 1, 1],
	    monitor="testMonitor",
	    allowGUI=1
	    )



for im in files:
	label=im
	im=loc+im
	
	#image stimulus
	img=visual.ImageStim(win=win,image=im, pos=[0,150],size=(400,400))

	#reference line
	#initial deviation
	dev=randint(-s,s)
	refline=visual.Line(win=win,start=(-99,-100),end=(77+dev,-100),lineColor='black',lineWidth=3)

	#the rating scale object
	ratingScale = visual.RatingScale(win=win, low=1, high=range ,pos=[0,-230],
		precision=10, scale='Length Scale', acceptText="Apply!!", showValue=0,
		lineColor="white", textColor="White", markerStart=(range-1.0)*(dev/(2.0*s)+0.5), 
		marker='circle', markerColor='grey', size=0.75)

	while ratingScale.noResponse:
		img.draw()
		ratingScale.draw()
		rate=ratingScale.getRating()
		#r1=visual.Line(win=win,start=(77,-10),end=(77,200),lineColor='black',lineWidth=3)
		#r2=visual.Line(win=win,start=(-99,-10),end=(-99,200),lineColor='black',lineWidth=3)

		if  rate!=rate1:
			refline=visual.Line(win=win,start=(-99-((2.0*(rate-1.0)
				/(range-1))-1)*(s/2.0),-100),end=(77+((2.0*(rate-1.0)
				/(range-1))-1)*(s/2.0),-100
				),lineColor='black',lineWidth=3)
		refline.draw()
		#r1.draw()
		#r2.draw()
		win.flip()
		rate1=rate


	#disparity
	disp=(2.0*(rate-1)/(range-1)-1)*s
	print(int(round(disp)))
	file.write("%d,%s\n" %(int(round(disp)),label))

file.close()
win.close()


# rating_subj = visual.RatingScale(win=win, name='rating_subj', pos=[1, 1], scale='Length',precision=100)

# positions = range(10)
# # random.shuffle(positions)
# # start = positions[0] + 1
# # rating_avrg = visual.RatingScale(win=win, name='rating_avrg', pos=[0.4, 0.4], scale='group',
# #     markerStart=str(start), minTime=0, maxTime=0.001)

# # rating_subj.draw()
# # win.flip()
# while rating_subj.noResponse:
#     rating_subj.draw()
#     a=rating_subj.getRating()
#     rating_avrg.draw()
#     win.flip()

# print(a)

# ratingScale = visual.RatingScale(win)
# item = [statement, question, image, movie]
# while ratingScale.noResponse:
#     item.draw()
#     ratingScale.draw()
#     win.flip()
# rating = ratingScale.getRating()
# decisionTime = ratingScale.getRT()
# choiceHistory = ratingScale.getHistory()
# print(rating)