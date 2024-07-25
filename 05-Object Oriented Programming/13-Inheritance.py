class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
class HeroIntelligence(Hero):
    pass

class HeroStrength(Hero):
    pass

lina = Hero("lina", 100)
techies = HeroIntelligence("techies", 100)
axe = HeroStrength("axe", 200)

print(lina.name)
print(techies.name)
print(axe.name)

"""
Output:

lina
techies
axe

"""