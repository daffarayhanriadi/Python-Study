from Hero import HeroIntelligence, HeroStrength

lina = HeroIntelligence("lina")
axe = HeroStrength("axe")

lina.show_info()
axe.show_info()

lina.gain_exp = 200
axe.gain_exp = 250

lina.show_info()
axe.show_info()

"""
Output:

lina 
        level: 1 
        health: 50 
        attPower: 20 
        armor: 0.5
axe 
        level: 1 
        health: 200 
        attPower: 20 
        armor: 2
lina level up!
axe level up!
lina
        level: 3
        health: 150
        attPower: 60
        armor: 1.5
axe
        level: 3
        health: 400
        attPower: 60
        armor: 6

"""