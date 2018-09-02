from soundstools import playSound,playWinbip,time,saveText,countDuration


# Class Viniasa 
class Viniasa:
    
    viniasaNum = 0
    viniasaBreath = 3

    def __init__ (self,viniasaNum,viniasaBreath=3):
        self.viniasaNum = viniasaNum
        self.viniasaBreath = viniasaBreath

    def execute(self):
        print ("Execute ", "Viniasa")
        i = 1
        
        while i <=  self.viniasaNum:     
   #         time.clock(self.viniasaBreath)
            if i%2 > 0: 
                playSound("Inhale")
            else: 
                playSound("Exhale")
            i = i + 1   
            countDuration(self.viniasaBreath)
            #print (time.clock(), " seconds process time")

# Class Asana
class Asana:
    
    Name = "Asana"
    Description = ""
    preViniasaNum = 3
    postViniasaNum = 3

    AsanaDuration = 30
    BreathSecs = 0

    def __init__(self,duration):
        self.AsanaDuration = duration
    def setBreathCount(self,secs):
        print("Breath Count")
        self.BreathSecs = secs
    def setPreViniasaNum(self,preViniasaNum=3):
        self.preViniasaNum = preViniasaNum
    def setPostViniasaNum(self,postViniasaNum=3):
        self.postViniasaNum = postViniasaNum

class Practice(Asana):
    
    def __init__(self,name="practice",description="Asana",duration=0):
        
        self.Name = name
        self.Description = description
        self.AsanaDuration = duration
        self.preViniasa = Viniasa(self.preViniasaNum)
        self.postViniasa = Viniasa(self.postViniasaNum)

    def __str__(self):
        return self.Name

    def __list__(self):
        return [self.Name,self.Description]

    def getDescription(self):
        return self.Description
        
    def runViniasa(self,num):
        viniasa = Viniasa(num,self.BreathSecs)
        viniasa.execute()
    def CreateVoiceName(self):
        saveText(self.getDescription(),self.Name)
    def SayMyName(self):
        playSound(self.Name)
        time.sleep(3)
              
    def execute(self):
        
        print ("Execute ", self.Name)
        time.clock()
        self.runViniasa(self.preViniasaNum)
#        playSound("Inhale")
        countDuration(self.AsanaDuration)
        #print (time.clock(),self.Name, " seconds process time (Practice)")
        self.runViniasa(self.postViniasaNum)
 #       playSound("Exhale")
        #print (time.clock(), "seconds process time")

def generalAsanaCount(numOfAsanas):
    
    i = 0
    while i < numOfAsanas:
        # measure process time
        time.clock()
        countDuration(30)        
        #print (time.clock(), "seconds process time")
        playSound("Inhale")
        countDuration(7)
        playSound("Exhale")
        #print (time.clock(), "seconds process time")

def asanaIteration(asana,num):
    
    i = 1
    while i <= num:
        if num > 1:
            playSound(str(i))
            time.sleep(3)
        print("Asana:" , str(i))
        asana.execute()
        i = i + 1
    
def sunSalutationA(numOfInstances):
    Sun1 = Practice("SunSalutationA","Sun Salutation A",30)
    Sun1.CreateVoiceName()
    Sun1.SayMyName()
    playSound(str(numOfInstances))
    playSound("Times")
    Sun1.setBreathCount(4)    
    Sun1.setPreViniasaNum(6)
    Sun1.setPostViniasaNum(4)
    asanaIteration(Sun1,numOfInstances)

def sunSalutationB(numOfInstances):
    Sun2 = Practice("SunSalutationB","Sun Salutation B",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(4)
    Sun2.setPreViniasaNum(14)
    Sun2.setPostViniasaNum(4)
    asanaIteration(Sun2,numOfInstances)

def padangusthasana(numOfInstances):
    Sun2 = Practice("Padangusthasana","Pada angoostha ausana",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(4)
    Sun2.setPostViniasaNum(2)
    asanaIteration(Sun2,numOfInstances)

def padanhastaasana(numOfInstances):
    Sun2 = Practice("Padanhastaasana","Pada hasta ausana ",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)
    asanaIteration(Sun2,numOfInstances)

def utthitatrikonasanaA(numOfInstances):
    Sun2 = Practice("UtthitatrikonasanA","ootthita treekona ausana  a",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)

def utthitatrikonasanaB(numOfInstances):
    Sun2 = Practice("UtthitatrikonasanaB","ootthita treekona ausana  b",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)
    
def utthitatrikonasanaC(numOfInstances):
    Sun2 = Practice("UtthitatrikonasanaC","ootthita treekona ausana  c",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)
    
def utthitatrikonasanaD(numOfInstances):
    Sun2 = Practice("UtthitatrikonasanaD","ootthita treekona ausana  d",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)

    
def utthitaparsvakonasana(numOfInstances):
    Sun2 = Practice("utthitaparsvakonasana","ootthita parshvakona ausana ",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(0)   
    asanaIteration(Sun2,numOfInstances)    

def parivrittaparsvakonasana(numOfInstances):
    Sun2 = Practice("utthitaparsvakonasana","Parivritta parshvakona ausana ",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)    


def prasaritapadottanasanaA(numOfInstances):
    Sun2 = Practice("prasaritapadottanasanaA","prasarita paadottana ausana  a",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)

def prasaritapadottanasanaB(numOfInstances):
    Sun2 = Practice("prasaritapadottanasanaB","prasarita paadottana ausana  b",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)
    
def prasaritapadottanasanaC(numOfInstances):
    Sun2 = Practice("prasaritapadottanasanaC","prasarita paadottana ausana  c",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)
    
def prasaritapadottanasanaD(numOfInstances):
    Sun2 = Practice("prasaritapadottanasanaD","prasarita paadottana ausana  d",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)

def parsvotanasana(numOfInstances):
    Sun2 = Practice("Parsvotanasana","Parshva oo tana ausana",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(2)   
    asanaIteration(Sun2,numOfInstances)

def utthitahastapadangusthasanaA(numOfInstances):
    Sun2 = Practice("utthitahastapadangusthasanaA","ootthitaa haasta paada aangoostha ausana  a",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(1)   
    asanaIteration(Sun2,numOfInstances)

def utthitahastapadangusthasanaB(numOfInstances):
    Sun2 = Practice("utthitahastapadangusthasanaB","ootthitaa haasta paada aangoostha ausana  b",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(1)   
    asanaIteration(Sun2,numOfInstances)
    
def utthitahastapadangusthasanaC(numOfInstances):
    Sun2 = Practice("utthitahastapadangusthasanaC","ootthitaa haasta paada aangoostha ausana  c",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(1)   
    asanaIteration(Sun2,numOfInstances)
    
def utthitahastapadangusthasanaD(numOfInstances):
    Sun2 = Practice("utthitahastapadangusthasanaD","ootthitaa haasta paada aangoostha ausana  d",30)
    Sun2.CreateVoiceName()
    Sun2.SayMyName()
    Sun2.setBreathCount(3)
    Sun2.setPreViniasaNum(2)
    Sun2.setPostViniasaNum(1)   
    asanaIteration(Sun2,numOfInstances)


