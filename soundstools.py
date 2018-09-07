import winsound
import time
from pygame import mixer # Load the required library
import sys
from gtts import gTTS

frequency = 2000  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
frequency_soft = 1000  # Set Frequency To 2500 Hertz
duration_soft = 100  # Set Duration To 1000 ms == 1 second
output_voices = "voices"


def playSound(filename):
    mixer.init(frequency=22050, size=-16, channels=2, buffer=4096)
    mixer.music.load(output_voices + "\\" + str(filename+".mp3"))
    mixer.music.play()


def save_text(mytext,filename):
    tts = gTTS(text=mytext, lang='en')
    tts.save(output_voices + "\\" + filename + ".mp3")
    print("Creating ", filename , "for: ",mytext)
    sys.stdout.flush()
    

def createSounds():
    
    i = 1
    while (i <= 30):
        save_text(str(i) + " Seconds.",str(i)+"Secs")
        i = i + 1
    i = 1
    while (i <= 10):
        save_text(str(i),str(i))
        i = i + 1

    save_text('Inhale','Inhale')
    save_text('Exhale','Exhale')
    save_text('Breathe for the next','takeBreath')
    save_text('seconds.','seconds')
    save_text('Lets start with Sun Salutation A','SunSalutationA')
    save_text('Sun Salutation B','SunSalutationB')
    save_text("Pada angoostha asana","Padangusthasana")
    save_text("Pada hasta asana","Padanhastaasana")
    save_text("Utthita trikona asana A","UtthitatrikonasanaA")
    save_text("Parsvo Utana Asana","Parsvotanasana")
    save_text('Times','Times')   


def count_duration(secs):
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
