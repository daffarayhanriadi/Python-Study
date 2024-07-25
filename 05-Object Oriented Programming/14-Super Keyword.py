'''
Seorang programmer harus menghindari pengulangan dalam pembuatan kode nya

Penggunaan **super()** lebih fleksibel ketika nama super class nya diganti
'''

class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def showInfo(self):
        print(f"{self.name} dengan health {self.health}")
        
class HeroIntelligence(Hero):
    def __init__(self, name):
        super().__init__(name, 100)
        super().showInfo()
        ## Hero.__init__(self, name, 100)
        # self.name = name
        # self.health = 100

class HeroStrength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)
        super().showInfo()
        ## Hero.__init__(self, name, 200)
        # self.name = name
        # self.health = 200
        
lina = HeroIntelligence("lina")
axe = HeroStrength("axe")

print(lina.health)
print(axe.health)

"""
Output:

lina dengan health 100
axe dengan health 200
100
200

"""