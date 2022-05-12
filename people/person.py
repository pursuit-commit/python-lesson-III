from enum import Enum

def mj(): 
    print('he he')

def elton():
    print('Rocket MANNnnnnaaannnn')

def drake():
    print('Kiki, do you love me?')

class AgeGroup(Enum):
    CHILD = 1
    ADULT = 2

class Person():
    def __init__(self, age, name): 
        self.name = name
        if age < 0:
            raise ValueError('Age cannot be negative.')
        else:
            self.age = age
            self.set_age_group(age) 

    def set_age_group(self, age):
        if age < 18:
            self.age_group = AgeGroup.CHILD
        else:
            self.age_group = AgeGroup.ADULT
    
    def set_age(self, age):
        if age < 0:
            raise ValueError('Age cannot be negative.')
        else:
            self.age = age
            self.set_age_group(age)  

    def get_age(self):
        return self.age

    def get_age_group(self):
        return self.age_group
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def jukebox(self, selection):
        if selection == 1:
            mj()
        elif selection == 2:
            elton()
        elif selection == 3:
            drake()
        else:
            raise ValueError('Jukebox only has 3 options')