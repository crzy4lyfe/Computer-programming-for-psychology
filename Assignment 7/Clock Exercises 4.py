from psychopy import visual, monitors, event, core
import os
start_msg='Welcome to my experiment'
mon=monitors.Monitor('myMonitor',width=12.1,distance=7)  
mon.setSizePix([1024,768])
win=visual.Window(monitor=mon) 
main_dir=os.getcwd() 
image_dir=os.path.join(main_dir,'images')
fix_text=visual.TextStim(win,text='+') 
stims=['face01.jpg','face02.jpg','face03.jpg','face04.jpg','face05.jpg','face06.jpg','face07.jpg','face08.jpg','face09.jpg','face10.jpg']
my_image=visual.ImageStim(win)
nTrials=4 
waitTimer=core.Clock() 
waitTimer.getTime() 
stimTimer=core.CountdownTimer()
#=====================
#BLOCK SEQUENCE
#=====================
nBlocks=2
nTrials=3
blockTimer=core.Clock()
trialTimer=core.Clock()
stimTimer=core.Clock()
for block in range(nBlocks):
    blockTimer.reset()
    blockStart=blockTimer.getTime()
#=====================
#TRIAL SEQUENCE
#=====================    
for trial in range(nTrials): 
    trialTimer.reset()
    trialStart=trialTimer.getTime()
    my_image.image=os.path.join(image_dir,stims[trial])
#=====================
    #START TRIAL
    #===================== 
    #-draw fixation
    fix_text.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(2)
    stimTimer.reset() 
    while stimTimer.getTime() <= 2:    
    #-draw image
    my_image.draw()
    #-flip window
    win.flip()
    imgStartTime=waitTimer.getTime()
    #-wait time (stimulus duration)
    core.wait(2)
    imgEndTime=waitTimer.getTime()
     print('Stimuli'+ str(trial) + 'time =', stimTimer.getTime())    
    #-draw end trial text
    endtr_msg="End of trial"
    endtr_text=visual.TextStim(win, text = endtr_msg)
    endtr_text.draw()
    #-flip window
    win.flip() 
    #-wait time (stimulus duration)
    core.wait(2)
    print('Trial'+str(trial)+' time =', trialTimer.getTime()) 
    print('Block'+str(block)+' time =', blockTimer.getTime()) 
#======================
# END OF EXPERIMENT
#======================
win.close() 