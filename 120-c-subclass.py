rom random import randint

class Player:

    def __init__(self, name):
    "The `constructor runs when we create a new thing"

        self.name = name
        self.jersey = randint(1, 99)

class Pitcher(Player):

    def __init__(self, name):
        super().__init__(name)
        self.strikeouts = 0

    def pitch_mph(____):
        mph = randint(50, 80)
        _____ mph 

    def strikeout(self):
        """Call this when pitcher throws a strikeout."""

        # Can you write this function?


    

pitcher = Pitcher('Thel')
print(pitcher.name, ' throws a strikeout!')
pitcher.strikeout()
print('She now has ', pitcher.strikeouts, ' strikeouts')
