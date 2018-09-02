import winsound
import time
from pygame import mixer # Load the required library
import sys
from gtts import gTTS
import os

frequency = 2000  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
frequency_soft = 1000  # Set Frequency To 2500 Hertz
duration_soft = 100  # Set Duration To 1000 ms == 1 second
output_voices = "voices"

def playSound(filename):
    mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    mixer.music.load(output_voices + "\\" + str(filename+".mp3"))
    mixer.music.play()
  
def saveText(mytext,filename):
    tts = gTTS(text=mytext, lang='en')
    tts.save(output_voices + "\\" + filename + ".mp3")
    print("Creating ", filename , "for: ",mytext)
    sys.stdout.flush()
    

def createSounds():
    
    i = 1
    while (i <= 30):
        saveText(str(i) + " Seconds.",str(i)+"Secs")
        i = i + 1
    i = 1
    while (i <= 10):
        saveText(str(i),str(i))
        i = i + 1

    saveText('Inhale','Inhale')
    saveText('Exhale','Exhale')
    saveText('Breathe for the next','takeBreath')
    saveText('seconds.','seconds')
    saveText('Lets start with Sun Salutation A','SunSalutationA')
    saveText('Sun Salutation B','SunSalutationB')
    saveText("Pada angoostha asana","Padangusthasana")
    saveText("Pada hasta asana","Padanhastaasana")
    saveText("Utthita trikona asana A","UtthitatrikonasanaA")
    saveText("Parsvo Utana Asana","Parsvotanasana")
    saveText('Times','Times')   


def countDuration(secs):
    i = 0
    
    if secs > 10:
        playSound('takeBreath')
        time.sleep(2)
        playSound(str(secs))        
        secs = secs -2
    
    while i < secs:
       time.sleep(1)
       i = i + 1
       sys.stdout.write('.')
       sys.stdout.flush()
    print (" Finished " , i ," Secs")

def playWinbip():
    winsound.Beep(frequency_soft, duration_soft)
