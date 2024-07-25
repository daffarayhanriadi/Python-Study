class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print("showInfo di Class Hero")
        print(f"{self.name} health : {self.health}")
    
class HeroIntelligence(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
    
    # Override showInfo Method
    def showInfo(self):
        print("showInfo di SubClass HeroIntelligence")
        print(f"{self.name} \n\ttype: intelligence \n\thealth: {self.health}")
        
class HeroStrength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        
lina = HeroIntelligence("lina")
axe = HeroStrength("axe")

lina.showInfo()
axe.showInfo()

"""
Output:

showInfo di SubClass HeroIntelligence
lina 
        type: intelligence 
        health: 100
showInfo di Class Hero
axe health : 200

"""