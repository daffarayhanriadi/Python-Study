class Hero:
    
    __jumlah = 0
    
    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0
        
        self.__healthMax = self.__healthBase * self.__level
       
        self.__attPower = self.__attPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level
        self.__health = self.__healthMax
        
        Hero.__jumlah += 1
        
    @property
    def info(self):
        return f"{self.__name} : \n\thealth = {self.__health}/{self.__healthMax} \n\tattack = {self.__attPower} \n\tarmor = {self.__armor}"
        
    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(f"{self.__name} level up!")
            self.__level += 1
            self.__exp -= 100
            
            self.__healthMax = self.__healthBase * self.__level
            self.__attPower = self.__attPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level
    
    def attack(self, lawan):
        self.gainExp = 50
        
slark = Hero("slark", 100, 10, 5)
axe = Hero("axe", 100, 5, 10)
print(slark.info)

slark.attack(axe)
slark.attack(axe)
print(slark.info)

"""
Output:

slark : 
        health = 100/100 
        attack = 10 
        armor = 5
slark level up!
slark : 
        health = 100/200 
        attack = 20 
        armor = 10

"""