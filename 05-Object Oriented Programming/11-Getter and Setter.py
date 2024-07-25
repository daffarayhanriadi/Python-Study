'''
Variable info dapat dengan mudah dirubah value nya, padahal kita ingin variable tersebut tetap valuenya.

Kalau misal variable tersebut di buat menjadi private, maka nanti nya tidak akan dapat diakses.

Kalau misal variable tersebut jadi private dan kita membuat getter nya, maka variable tersebut
berubah menjadi method.

Disinilah kegunaan dari decorator property (@property) --> adalah dekorator yang digunakan untuk 
mendefinisikan metode getter dalam kelas, memungkinkan kita untuk mengakses metode tersebut seperti 
atribut biasa.

Jika kita lihat melalui print(sniper.__dict__), @property tidak akan dideteksi sebagai variable,
karena ia adalah sebuah method yang dianggap sebagai variable.

Keunggulan dari @property adalah dapat terus update saat program sedang berjalan.

---

Sebelum kita masuk getter & setter dalam enkapsulasi, kita harus menganggap si variable yang ingin
kita ambil itu adalah sebagai @property. 
'''

class Hero():
    def __init__(self, name, health, armor):
        self.__name = name
        self.__health = health
        self.__armor = armor
        # self.info = f"name {self.name} : \n\thealth: {self.__health}" # ini hanya update 1x saat awal penggunaan __init__

    @property
    def info(self):
        return f"name {self.__name} : \n\thealth: {self.__health}"
    
    @property
    def health(self):
        pass
    
    @property # @property digunakan ketika ingin mendefinisikan method Getter dan Setter
    def armor(self):
        pass
    
    # getter
    @armor.getter
    def armor(self):
        return self.__armor
    
    # setter
    @armor.setter
    def armor(self, input):
        self.__armor = input
    
    # deleter
    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None
    
    @health.getter
    def health(self):
        return self.__health
    
    # Getter Tradisional (masih terlihat seperti method saat dipanggil)
    def get_health(self):
        return self.__health

sniper = Hero("Sniper", 100, 10)
print(sniper.info)
# sniper.name = "Ucup"
# print(sniper.info)

print("\ngetter dan setter untuk __armor:")
print(sniper.armor) # Bisa ditampilkan karena adanya GETTER modern
print(sniper.__dict__)
sniper.armor = 50 # Bisa diubah karena adanya SETTER modern
print(sniper.armor)

print("\ndelete armor")
del sniper.armor
print(sniper.__dict__)

# Getter dengan cara tradisional
print("\ngetter tradisional")
print(sniper.get_health())

# Getter dengan cara terbaru
print("\ngetter terbaru")
print(sniper.health)

"""
Output:

name Sniper : 
        health: 100

getter dan setter untuk __armor:
10
{'_Hero__name': 'Sniper', '_Hero__health': 100, '_Hero__armor': 10}
50

delete armor
armor di delete
{'_Hero__name': 'Sniper', '_Hero__health': 100, '_Hero__armor': None}

getter tradisional
100

getter terbaru
100

"""