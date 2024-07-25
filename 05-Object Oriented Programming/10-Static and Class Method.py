class Hero():
    
    __jumlah = 0
    
    def __init__(self, name):
        self.name = name
        Hero.__jumlah += 1
        
    # Method yang hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    
    # Method yang hanya berlaku untuk class
    def getJumlah1():
        return Hero.__jumlah
    
    # method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    # Method class (decorator) nempel ke objek dan class serta lebih fleksibel daripada static
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
sniper = Hero("Sniper")
riki = Hero("Riki")
drow = Hero("Drow")

print(sniper.getJumlah())

# print(Hero.getJumlah()) # Error
# print(sniper.getJumlah1()) # Error

print(Hero.getJumlah1())

print(sniper.getJumlah2())
print(Hero.getJumlah2())

print(sniper.getJumlah3())
print(Hero.getJumlah3())

"""
Output:

3
3
3
3
3
3

"""