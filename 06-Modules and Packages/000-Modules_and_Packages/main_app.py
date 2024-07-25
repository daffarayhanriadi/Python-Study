"""
Saat kita import sains, dia itu tidak punya apapun karena hanya berupa sebuah folder, maka dari itu
kita butuh __init__.py untuk melekatkan module yang dibutuhkan untuk melakukan import
    
"""

from sains.matematika import scientific # tetap bisa walau tanpa __init__.py
import sains

# hasil_tambah = sains.matematika.basic.tambah(1,2,3,4,5)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_kali = sains.matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = sains.matematika.kali(1,3,4,5,6)
print(f"hasil kali = {hasil_kali}")

pangkat_2 = scientific.pangkat(2) ##
print(f"hasil pangkat = {pangkat_2(5)}")

hasil_fisika = sains.fisika.gaya(10, 9.8)
print(f"hasil gaya = {hasil_fisika}")



# from sains import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,5)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_kali = matematika.basic.kali(1,3,4,5,6)
# print(f"hasil kali = {hasil_kali}")

# hasil_fisika = fisika.gaya(10, 9.8)
# print(f"hasil gaya = {hasil_fisika}")