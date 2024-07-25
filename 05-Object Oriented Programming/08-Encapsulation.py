class Hero:
    def __init__(self, name, health, attPower):
        self.__name = name
        self.__health = health
        self.__attPower = attPower
    
    # Getter
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    
    # Setter
    def diserang(self, serangPower):
        self.__health -= serangPower
        
    def set_attPower(self, nilai_baru):
        self.__attPower = nilai_baru
        
# Awal dari game
earthshaker = Hero("earthshaker", 50, 5)

# Game berjalan
print(earthshaker.get_name())
print(earthshaker.get_health())
earthshaker.diserang(5)
print(earthshaker.get_health())

"""
Output:

earthshaker
50
40

"""