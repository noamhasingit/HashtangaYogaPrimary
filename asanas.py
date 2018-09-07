from soundstools import playSound, playWinbip, time, save_text, count_duration


# Class Viniasa 
class Viniasa:
    
    viniasaNum = 0
    viniasa_breath = 3

    def __init__(self, num, viniasa_breath=3):
        self.viniasaNum = num
        self.viniasa_breath = viniasa_breath

    def execute(self):
        print("Execute ", "Viniasa")
        i = 1
        
        while i <= self.viniasaNum:
   #         time.clock(self.viniasa_breath)
            if i%2 > 0: 
                playSound("Inhale")
            else:
                playSound("Exhale")
            i = i + 1   
            count_duration(self.viniasa_breath)
            #print (time.clock(), " seconds process time")

# Class Asana
class Asana:
    
    Name = "Asana"
    Description = ""
    pre_viniasaNum = 3
    post_viniasaNum = 3

    asana_duration = 30
    BreathSecs = 0

    def __init__(self,duration):
        self.asana_duration = duration

    def set_breath_count(self, secs):
        print("Breath Count")
        self.BreathSecs = secs

    def set_pre_viniasa_num(self, pre_viniasaNum=3):
        self.pre_viniasaNum = pre_viniasaNum

    def set_post_viniasa_num(self, post_viniasaNum=3):
        self.post_viniasaNum = post_viniasaNum


class Practice(Asana):
    
    def __init__(self, name="practice", description="Asana", duration=0):
        
        Asana.__init__(self, duration)
        self.Name = name
        self.Description = description
        self.asana_duration = duration
        self.pre_viniasa = Viniasa(self.pre_viniasaNum)
        self.post_viniasa = Viniasa(self.post_viniasaNum)

    def __str__(self):
        return self.Name

    def __list__(self):
        return [self.Name, self.Description]

    def get_description(self):
        return self.Description
        
    def run_viniasa(self, num):
        viniasa = Viniasa(num, self.BreathSecs)
        viniasa.execute()
        
    def create_voice_name(self):
        save_text(self.get_description(), self.Name)
        
    def say_my_name(self):
        playSound(self.Name)
        time.sleep(3)
              
    def execute(self):
        
        print ("Execute ", self.Name)
        time.clock()
        self.run_viniasa(self.pre_viniasaNum)
#        playSound("Inhale")
        count_duration(self.asana_duration)
        #print (time.clock(),self.Name, " seconds process time (Practice)")
        self.run_viniasa(self.post_viniasaNum)
 #       playSound("Exhale")
        #print (time.clock(), "seconds process time")

def general_asana_count(numOfAsanas):
    
    i = 0
    while i < numOfAsanas:
        # measure process time
        time.clock()
        count_duration(30)        
        #print (time.clock(), "seconds process time")
        playSound("Inhale")
        count_duration(7)
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

    
def sunSalutationA(instance_num):

    Sun1 = Practice("SunSalutationA", "Surya Namaskara A",30)
    Sun1.create_voice_name()
    Sun1.say_my_name()
    playSound(str(instance_num))
    playSound("Times")
    Sun1.set_breath_count(4)    
    Sun1.set_pre_viniasa_num(6)
    Sun1.set_post_viniasa_num(4)
    asanaIteration(Sun1,instance_num)


def sunSalutationB(instance_num):
    Sun2 = Practice("SunSalutationB", "Surya Namaskara B",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(4)
    Sun2.set_pre_viniasa_num(14)
    Sun2.set_post_viniasa_num(4)
    asanaIteration(Sun2,instance_num)

def padangusthasana(instance_num):
    Sun2 = Practice("Padangusthasana", "Pada angoostha ausana",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(4)
    Sun2.set_post_viniasa_num(2)
    asanaIteration(Sun2,instance_num)

def padanhastaasana(instance_num):
    
    Sun2 = Practice("Padanhastaasana", "Pada hasta ausana ",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)
    asanaIteration(Sun2,instance_num)


def utthitatrikonasanaA(instance_num):

    Sun2 = Practice("UtthitatrikonasanA", "ootthita treekona ausana  a",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)


def utthitatrikonasanaB(instance_num):

    Sun2 = Practice("UtthitatrikonasanaB", "ootthita treekona ausana  b",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)


def utthitatrikonasanaC(instance_num):

    Sun2 = Practice("UtthitatrikonasanaC", "ootthita treekona ausana  c",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)
    

def utthitatrikonasanaD(instance_num):
    Sun2 = Practice("UtthitatrikonasanaD", "ootthita treekona ausana  d",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)

    
def utthitaparsvakonasana(instance_num):
    Sun2 = Practice("utthitaparsvakonasana", "ootthita parshvakona ausana ",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(0)   
    asanaIteration(Sun2,instance_num)    


def parivrittaparsvakonasana(instance_num):
    Sun2 = Practice("utthitaparsvakonasana", "Parivritta parshvakona ausana ",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)    


def prasaritapadottanasanaA(instance_num):
    Sun2 = Practice("prasaritapadottanasanaA", "prasarita paadottana ausana  a",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)


def prasaritapadottanasanaB(instance_num):
    Sun2 = Practice("prasaritapadottanasanaB", "prasarita paadottana ausana  b",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)
    

def prasaritapadottanasanaC(instance_num):
    Sun2 = Practice("prasaritapadottanasanaC", "prasarita paadottana ausana  c",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)
    

def prasaritapadottanasanaD(instance_num):
    Sun2 = Practice("prasaritapadottanasanaD", "prasarita paadottana ausana  d",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)


def parsvotanasana(instance_num):
    Sun2 = Practice("Parsvotanasana", "Parshva oo tana ausana",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(2)   
    asanaIteration(Sun2,instance_num)


def utthitahastapadangusthasanaA(instance_num):
    Sun2 = Practice("utthitahastapadangusthasanaA", "ootthitaa haasta paada aangoostha ausana  a",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(1)   
    asanaIteration(Sun2,instance_num)


def utthitahastapadangusthasanaB(instance_num):
    Sun2 = Practice("utthitahastapadangusthasanaB", "ootthitaa haasta paada aangoostha ausana  b",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(1)   
    asanaIteration(Sun2,instance_num)
    

def utthitahastapadangusthasanaC(instance_num):
    Sun2 = Practice("utthitahastapadangusthasanaC", "ootthitaa haasta paada aangoostha ausana  c",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(1)   
    asanaIteration(Sun2,instance_num)
    

def utthitahastapadangusthasanaD(instance_num):
    Sun2 = Practice("utthitahastapadangusthasanaD", "ootthitaa haasta paada aangoostha ausana  d",30)
    Sun2.create_voice_name()
    Sun2.say_my_name()
    Sun2.set_breath_count(3)
    Sun2.set_pre_viniasa_num(2)
    Sun2.set_post_viniasa_num(1)   
    asanaIteration(Sun2,instance_num)


