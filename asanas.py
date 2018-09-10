from soundstools import playSound, playWinbip, time, save_text, count_duration, get_sound_file_path
from enum import Enum, auto
from pathlib import Path
import datetime

class Breath(Enum):
    EXHALE = auto()
    INHALE = auto()
    RIGHT = auto()
    LEFT = auto()


# Class Viniasa 
class Viniasa:
    
    viniasaNum = 0
    viniasa_breath = 3
    breath_order = Breath.INHALE

    def __init__(self, num, viniasa_breath=3, breath_order=Breath.INHALE):
        self.viniasaNum = num
        self.viniasa_breath = viniasa_breath
        self.breath_order = breath_order

    def execute(self):
        print("Execute ", "Viniasa")
        i = 1
        
        while i <= self.viniasaNum:
            # time.clock(self.viniasa_breath)
            if i % 2 > 0:
                if self.breath_order == Breath.INHALE:
                    playSound("Inhale")
                else:
                    playSound("Exhale")
            else:
                if self.breath_order == Breath.INHALE:
                    playSound("Exhale")
                else:
                    playSound("Inhale")
            i = i + 1
            count_duration(self.viniasa_breath)
            # print (time.clock(), " seconds process time")

# Class Asana
class Asana:
    
    Name = "Asana"
    Description = ""
    pre_viniasaNum = 3
    post_viniasaNum = 3
    breath_order = Breath.INHALE
    start_with_side = Breath.RIGHT

    asana_duration = 30
    BreathSecs = 0

    def __init__(self, duration):
        self.asana_duration = duration

    def set_breath_count(self, secs):
        print("Breath Count")
        self.BreathSecs = secs

    def set_pre_viniasa_num(self, pre_viniasaNum=2):
        self.pre_viniasaNum = pre_viniasaNum

    def set_post_viniasa_num(self, post_viniasaNum=2):
        self.post_viniasaNum = post_viniasaNum

    def set_breath_order(self, breath_order):
        self.breath_order = breath_order

    def set_start_with_side(self, side=Breath.RIGHT):
        self.start_with_side = side

    def get_start_side(self):
        return self.start_with_side


class Practice(Asana):

    def __init__(self, name="practice", description="Asana", duration=0):
        
        Asana.__init__(self, duration)
        self.Name = name
        self.Description = description
        self.asana_duration = duration
        self.pre_viniasa = Viniasa(self.pre_viniasaNum)
        self.post_viniasa = Viniasa(self.post_viniasaNum)
        self.start_prectice_time = time.clock()

    def __str__(self):
        return self.Name

    def __list__(self):
        return [self.Name, self.Description]

    def get_description(self):
        return self.Description
        
    def run_viniasa(self, num, start_with=Breath.INHALE):
        viniasa = Viniasa(num, self.BreathSecs, start_with)
        viniasa.execute()
        
    def create_voice_name(self, force=False):
        if force:
            save_text(self.get_description(), self.Name)
        else:
            my_file = Path(get_sound_file_path() + self.Name + ".mp3")
            if not my_file.is_file():
                save_text(self.get_description(), self.Name)

    def say_my_name(self):
        playSound(self.Name)
        time.sleep(3)


    def execute(self):

        print("Execute ", self.Name)
        time.clock()
        self.run_viniasa(self.pre_viniasaNum, self.breath_order)
#        playSound("Inhale")
        count_duration(self.asana_duration)
        #print (time.clock(),self.Name, " seconds process time (Practice)")
        self.run_viniasa(self.post_viniasaNum)
 #       playSound("Exhale")
        #print (time.clock(), "seconds process time")


def say_practice_time():
        start_practice_hour = datetime.datetime.time(datetime.datetime.now()).hour
        start_practice_minute = datetime.datetime.time(datetime.datetime.now()).minute

        save_text("Time is: " + str(start_practice_hour) + " and " + str(start_practice_minute) + " minutes","currentTime")
        playSound("currentTime")
        time.sleep(3)

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


def asana_iteration_by_num(asana, num):

    i = 1
    while i <= num:
        if num > 1:
            playSound(str(i))
            time.sleep(3)
        print("Asana:", str(i))
        asana.execute()
        i = i + 1


def asana_iteration_by_sides(asana, num):
    i = 1
    while i <= num:
        if num > 1:
            # print('debug', i, asana.get_start_side().value)
            if asana.get_start_side() is Breath.RIGHT:
                if i%2:
                    playSound('Right')
                else:
                    playSound('Left')
            elif asana.get_start_side() is Breath.LEFT:
                if i%2:
                    playSound('Left')
                else:
                    playSound('Right')
            time.sleep(3)
        print("Asana:", str(i))
        asana.execute()
        i = i + 1


def sunSalutationA(instance_num):

    my_practice = Practice("SunSalutationA", "Surya Namaskara A", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    playSound(str(instance_num))
    playSound("Times")
    my_practice.set_breath_count(4)    
    my_practice.set_pre_viniasa_num(6)
    my_practice.set_post_viniasa_num(4)
    asana_iteration_by_num(my_practice, instance_num)


def sunSalutationB(instance_num):

    my_practice = Practice("SunSalutationB", "Surya Namaskara B", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(4)
    my_practice.set_pre_viniasa_num(14)
    my_practice.set_post_viniasa_num(4)
    asana_iteration_by_num(my_practice, instance_num)

def padangusthasana(instance_num):

    my_practice = Practice("Padangusthasana", "Pada angoostha ausana", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(4)
    my_practice.set_post_viniasa_num(2)
    asana_iteration_by_num(my_practice, instance_num)

def padanhastaasana(instance_num):
    
    my_practice = Practice("Padanhastaasana", "Pada hasta ausana ", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(3)
    my_practice.set_post_viniasa_num(4)
    my_practice.set_breath_order(Breath.EXHALE)
    asana_iteration_by_num(my_practice, instance_num)


def utthitatrikonasana(instance_num):

    my_practice = Practice("Utthitatrikonasan", "ootthita treekona ausana.", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(2)
    my_practice.set_post_viniasa_num(0)
    asana_iteration_by_sides(my_practice, instance_num)


def parivrittatrikonasana(instance_num):

    my_practice = Practice("Parivrittatrikonasana", "parivritta treekona ausana.", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(2)
    my_practice.set_post_viniasa_num(0)
    my_practice.set_start_with_side(Breath.RIGHT)
    asana_iteration_by_sides(my_practice, instance_num)


def utthitaparsvakonasana(instance_num):
    my_practice = Practice("utthitaparsvakonasana", "ootthita parshvakona ausana.", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(2)
    my_practice.set_post_viniasa_num(0)
    asana_iteration_by_sides(my_practice, instance_num)


def parivrittaparsvakonasana(instance_num):
    my_practice = Practice("utthitaparsvakonasana", "Parivritta parshvakona ausana ", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(2)
    my_practice.set_post_viniasa_num(0)
    asana_iteration_by_sides(my_practice, instance_num)


def prasaritapadottanasanaA(instance_num):
    my_practice = Practice("prasaritapadottanasanaA", "prasarita paadottana ausana  a", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(4)
    my_practice.set_post_viniasa_num(2)   
    asana_iteration_by_num(my_practice, instance_num)


def prasaritapadottanasanaB(instance_num):
    my_practice = Practice("prasaritapadottanasanaB", "prasarita paadottana ausana  b", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(4)
    my_practice.set_post_viniasa_num(2)   
    asana_iteration_by_num(my_practice, instance_num)
    

def prasaritapadottanasanaC(instance_num):
    my_practice = Practice("prasaritapadottanasanaC", "prasarita paadottana ausana  c", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(4)
    my_practice.set_post_viniasa_num(2)   
    asana_iteration_by_num(my_practice, instance_num)
    

def prasaritapadottanasanaD(instance_num):
    my_practice = Practice("prasaritapadottanasanaD", "prasarita paadottana ausana  d", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(4)
    my_practice.set_post_viniasa_num(2)   
    asana_iteration_by_num(my_practice, instance_num)


def parsvotanasana(instance_num):
    my_practice = Practice("Parsvotanasana", "Parshva oo tana ausana", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(4)
    my_practice.set_post_viniasa_num(2)
    asana_iteration_by_sides(my_practice, instance_num)


def utthitahastapadangusthasanaA(instance_num):
    my_practice = Practice("utthitahastapadangusthasanaA", "uutthitaa haasta paada aangoostha ausana  a", 20)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(2)
    my_practice.set_post_viniasa_num(2)
    asana_iteration_by_num(my_practice, instance_num)


def utthitahastapadangusthasanaB(instance_num):
    my_practice = Practice("utthitahastapadangusthasanaB", "uutthitaa haasta paada aangoostha ausana  b", 20)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(0)
    my_practice.set_post_viniasa_num(2)
    asana_iteration_by_num(my_practice, instance_num)
    

def utthitahastapadangusthasanaC(instance_num):
    my_practice = Practice("utthitahastapadangusthasanaC", "uutthitaa haasta paada aangoostha ausana  c", 20)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(0)
    my_practice.set_post_viniasa_num(2)
    asana_iteration_by_num(my_practice, instance_num)
    

def utthitahastapadangusthasanaD(instance_num):
    my_practice = Practice("utthitahastapadangusthasanaD", "uutthitaa haasta paada aangoostha ausana  d", 20)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(0)
    my_practice.set_post_viniasa_num(2)
    asana_iteration_by_num(my_practice, instance_num)


def ardhabaddhapadmottanasana(instance_num):
    my_practice = Practice("ardhabaddhapadmottanasana", "ardha baddha padmottana ausana", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(4)
    my_practice.set_post_viniasa_num(2)
    asana_iteration_by_sides(my_practice, instance_num)


def utkatasana(instance_num):
    my_practice = Practice("utkatasana", "uutkata ausana", 30)
    my_practice.create_voice_name()
    my_practice.say_my_name()
    my_practice.set_breath_count(3)
    my_practice.set_pre_viniasa_num(6)
    my_practice.set_post_viniasa_num(4)
    asana_iteration_by_sides(my_practice, instance_num)


