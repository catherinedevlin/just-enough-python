# There is one bug in the `strikeout` method, 
# and a bunch of bugs in the lines at the bottom 
# that use the class!  

from random import randint

class Player:

    def __init__(self, name):
    "The `constructor runs when we create a new thing"

        self.name = name
        self.jersey = randint(1, 99)

class Pitcher(Player):

    def __init__(self, name):
        super().__init__(name)
        self.strikeouts = 0

    def pitch_mph(self):
        mph = randint(50, 80)
        return mph 

    def strikeout(self):
        """Call this when pitcher throws a strikeout."""

        strikeouts = strikeouts + 1
    

Pitcher = Player('Windy')
print(Pitcher.name, ' throws a strikeout!')
Pitcher.strikeout()
print('She now has ', Pitcher.strikeouts, ' strikeouts')
