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
stimTimer=core.Clock()
for trial in range(nTrials):
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
    imgStartTime=waitTimer.getTime()
    while stimTimer.getTime() <= 1:
        
    #-draw image
    my_image.draw()
    #-flip window
    win.flip()
    imgStartTime=waitTimer.getTime()
    #-wait time (stimulus duration)
    core.wait(2)
    imgEndTime=waitTimer.getTime()
        
    #-draw end trial text
    endtr_msg="End of trial"
    endtr_text=visual.TextStim(win, text = endtr_msg)
    endtr_text.draw()
    #-flip window
    win.flip() 
    #-wait time (stimulus duration)
    core.wait(2)
    
    print("Image Duration was {} seconds".format(imgEndTime-imgStartTime))
#Clock_wait_timer is not as precise as wait_timer. It measures image duration at a 10th of a second
#======================
# END OF EXPERIMENT
#======================
win.close() 