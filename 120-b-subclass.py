from random import randint

class Player:

    def __init__(self, name):
    "The `constructor runs when we create a new thing"

        self.name = name
        self.jersey = randint(1, 99)

class Pitcher(Player):

    def pitch_mph(____):
        mph = randint(50, 80)
        _____ mph 

thel = Pitcher('Thel')
print('Thel throws a ', thel.pitch_mph(), ' fastball')
