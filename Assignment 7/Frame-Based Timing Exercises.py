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
fixdur=0.2 
imagedur=1.0
textdur=0.5 
refresh = 1.0/60.0
fixframes=int(fixdur/refresh)
imageframes=int(imagedur/refresh) 
textframes=int(textdur/refresh) 
totalframes=int(fixframes+imageframes+textframes)
fix=visual.TextStim(win,text='+')
win.recordFrameIntervals=True 

#=====================
#BLOCK SEQUENCE
#=====================
nBlocks=2
nTrials=3

for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames):
            #-draw stimulus
            if 0<=frameN<=fix_frames: 
                win.flip()
                if frameN==fix_frames: 
                    print("End fix frame =",frameN) 
            if fix_frames<frameN<=(fix_frames+image_frames):      
                fix.draw()
                win.flip() 
                if frameN==(fix_frames+image_frames): 
                    print("End image frame =",frameN) 
            if (fix_frames+image_frames)<frameN<total_frames:  
                fix.draw()
                win.flip() 
                if frameN==(total_frames-1): 
                    print("End text frame =",frameN) 
            
    print('Overall,%i frames were dropped.'% win.nDroppedFrames)
                
win.close()  
#adding a dropped frame detector shows that no frames are dropped in the experiment              
#======================
# END OF EXPERIMENT
#======================
win.close() 