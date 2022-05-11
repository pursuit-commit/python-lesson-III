def side_effect(color):
    print('side effect caused')

class Dog():
    def __init__(self, name, breed, age, color) -> None:
        self.name = name
        self.age = age
        self.color = color

        if (breed == ''):
            # print('do nothing')
            raise Exception('Breed was provided as empty string')
        else:
            self.breed = breed
    
    def get_name(self): 
        return self.name
    
    def get_breed(self):
        return self.breed

    def get_age(self):
        return self.age

    def get_info(self):
        return self.get_info_side_effect()

    def get_info_side_effect(self):
        return 'something'
    
    def age_in_dog_years(self):
        return self.age * 7

    def get_color(self):
        return self.color
    
    
    def set_color(self, color):
        self.color = color
        side_effect()

    def __str__(self):
        return 'Hi my name is ' + self.name + '... bark!'