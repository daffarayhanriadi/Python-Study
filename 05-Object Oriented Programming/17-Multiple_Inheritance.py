class Team:
    def set_team(self, team):
        self.team = team
        
    def show_team(self):
        print(self.team)


class HeroType:
    def set_type(self, type): #bagaimana jika nama method nya sama? -> Method Resolution Order
        self.type = type
    
    def show_type(self):
        print(self.type)


class Hero(Team, HeroType):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
snapfire = Hero("snapfire", 100)
snapfire.set_team("merah")
snapfire.set_type("range")

snapfire.show_team()
snapfire.show_type()

"""
Output:

merah
range

"""