class Mangga:
    
    # Magic Method
    def __init__(self, name, jumlah):
        self.name = name
        self.jumlah = jumlah
        
    def __repr__(self): # Biasanya digunakan saat sedang melakukan debugging
        return "Debug - Mangga: {} dengan jumlah: {}".format(self.name, self.jumlah)
    
    def __str__(self): # Biasanya digunakan saat sudah dalam production
        return "Mangga: {} dengan jumlah: {}".format(self.name, self.jumlah)
    
    def __add__(self, objek): # Berguna saat ingin melakukan operasi
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self): # Bisa di override
        return "objek ini mempunyai nama dan jumlah"
    
belanja1 = Mangga("arumanis", 10)
belanja2 = Mangga("siasem", 5)
print(belanja1)
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)

"""
Output:

Mangga: arumanis dengan jumlah: 10
Mangga: siasem dengan jumlah: 5
15
objek ini mempunyai nama dan jumlah

"""