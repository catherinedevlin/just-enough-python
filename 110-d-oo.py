# Each of these methods has the same bug - 
# a mistake you'll make a thousand times.

class Team:

    def __init__(city, name):

        self.city = city 
        self.name = name 
        self.roster = [] 

    def draft(player):

        # ".append tacks an item onto a list.  Finish!"
        ___________.append(player)

    def __str__():
        "A 'magic method' called when we print!"

        return ____.city + " " + ____.name 

chicks = Team('Grand Rapids', 'Chicks')
print("Welcome " + chicks + "!")

chicks.draft('Tia')
print(chicks.roster)
