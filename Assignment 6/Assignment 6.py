#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event, monitors
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os
from datetime import datetime

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info={'subject_nr':0, 
            'age':'', 
            'handedness':('right','left','ambi'), 
            'gender':'',
            'session': 1}
print(exp_info)
my_dlg=gui.DlgFromDict(dictionary=exp_info,
                        title="subject info",
                        fixed=['session'],
                        order=['session','subject_nr','age','gender','handedness'])
#title for dialog box
my_dlg=gui.DlgFromDict(dictionary=exp_info,
                        title='subject info',
                        fixed=['session'],
                        order=['session','subject_nr','age','gender','handedness'])
print("All variables have been created! Now ready to show the dialog box!")
my_dlg.show()
    #setting the variable session as fixed makes it so that th participant cant change the value for this variable
#get date and time
date=datetime.now()
print(date)
exp_info['date']=str(date.hour)+'-'+str(date.day)+'-'+str(date.month)+'-'+str(date.year)
print(exp_info['date'])
#-create a unique filename for the data
filename=str(exp_info['subject_nr'])+'_'+exp_info['date']+'.csv'
#check if this data is correct
if exp_info['subject_nr']==0:
    err_dlg=gui.Dlg(title='error message')
    err_dlg.addText('Enter a valid subject number!')
    err_dlg.show()
    core.quit()
#participant consent to experiment
if exp_info['age'] <18:
    err_dlg=gui.Dlg(title='error message')
    err_dlg.addText('%d year olds cannot give consent!'%(exp_info['age']))
    err_dlg.show()
    core.quit()

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon=monitors.Monitor('myMonitor',width=12.1,distance=7)  
mon.setSizePix([1024,768])
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win=visual.Window(monitor=mon,
                    size=(800,800),
                    color=[-1,-1,-1],
                    units='pix',
                    fullscr=True)
#How does changing "units" affect how you define your window size?
    #changing the units affexts how the window size is defined because of what is being used to measure
#How does changing colorSpace affect how you define the color of your window? Can you define colors by name?
    #Changing colorSpace can affect how you define the color of your window because colorSpace can change the color of the window.
    #We can use different colorSpaces in psychopy such as RGB, DKL, LMS, HSV
        #each of these colorspaces uses different values to specify each color
    #yes colors can be defined by names, this is by using strings and colour names for example, stim.setColor('Firebrick')

#Stimulus Exercises
#question 1
main_dir=os.getcwd()
image_dir=os.path.join(main_dir,'images')
my_image=visual.ImageStim(win,units='pix',size=(400,400))
stims=['face1.jpg','face2.jpg','face3.jpg','face4.jpg','face5.jpg','face6.jpg','face7.jpg','face8.jpg','face9.jpg','face10.jpg']
nTrials=10 
for trial in range(nTrials): 
    my_image.image=os.path.join(image_dir,stims[trial])
    my_image.draw() 
    win.flip()
    event.waitKeys()  
win.close()
#question 2
vertMult=[1,1,-1,-1]
horizMult=[-1,1,-1,1]
for trial in range(nTrials):
    my_image.image=os.path.join(image_dir,stims[trial])
    my_image.pos=(horizMult[trial]*thisWidth/4,vertMult[trial]*thisHeight/4)
    my_image.draw()
    fix_text.draw()
    win.flip()
    event.waitKeys()
win.close()
#question 3
fix_text=visual.TextStim(win,text='+')
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define experiment start text unsing psychopy functions
start_msg='Welcome to my experiment'
#-define block (start)/end text using psychopy functions
block_msg="Press any key to continue to the next block."
end_trial_msg="End of trial"
#-define stimuli using psychopy functions (images, fixation cross)
stims=['face1.jpg','face2.jpg','face3.jpg','face4.jpg','face5.jpg','face6.jpg','face7.jpg','face8.jpg','face9.jpg','face10.jpg']
fix_text=visual.TextStim(win,text='+')
#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_text=visual.TextStim(win,text=start_msg)
start_text.draw()
win.flip()
#-allow participant to begin experiment with button press
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
nblocks=2
ntrials-10
#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
    block_text=visual.TextStim(win,text=block_msg)
    block_text.draw()
    win.flip()
    event.waitKeys()
    #-randomize order of trials here
    np.random.shuffle(stims)
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials)
        #-set stimuli and stimulus properties for the current trial
         my_image.image=os.path.join(image_dir,stims[trial])
         
        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw image
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys()
        
        #-draw end trial text
        end_trial_msg="End of trial"
        end_trial=visual.TextStim(win,text=end_trial_msg)
        end_trial.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        event.waitKeys() 
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
win.close()
#-quit experiment