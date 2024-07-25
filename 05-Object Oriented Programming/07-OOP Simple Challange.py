class Hero:
    def __init__(self, name, health, attPower, armor):
        self.name = name
        self.health = health
        self.attPower = attPower
        self.armor = armor
    
    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self)
    
    def diserang(self, lawan):
        print(f"{self.name} diserang {lawan.name}")
        serangan_diterima = lawan.attPower / self.armor
        print(f"Serangan terasa: {serangan_diterima}")
        self.health -= serangan_diterima
        print(f"Darah tersisa: {self.health}")
        
sniper = Hero("Sniper", 100, 10, 5)
riki = Hero("Riki", 100, 20, 10)

sniper.serang(riki)
print()
riki.serang(sniper)

"""
Output:

Sniper menyerang Riki
Riki diserang Sniper
Serangan terasa: 1.0
Darah tersisa: 99.0

Riki menyerang Sniper
Sniper diserang Riki
Serangan terasa: 4.0
Darah tersisa: 96.0

"""