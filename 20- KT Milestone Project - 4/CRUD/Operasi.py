from . import Database
from .Utils import random_string
import time
import os

def create(penulis, judul, tahun):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    # print(data_str)
    
    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal maning!")

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
        try: 
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan lagi (yyyy)")  
        except:
            print("Tahun harus angka, silahkan masukkan lagi (yyyy)")
    
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    # print(data_str)
    
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal masbro!")
        
def read(**kwargs):
    try:
        with open(Database.DB_NAME, "r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            # print(jumlah_buku)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("Membaca database error")
        return False

def update(no_buku, pk, date_add, penulis, judul, tahun):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis
    data["judul"] = judul
    data["tahun"] = tahun
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    data_length = len(data_str)
    
    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file:
            file.seek(data_length*(no_buku-1))
            file.write(data_str)
    except:
        print("Error dalam update data")

def delete(no_buku):
    try:
        with open(Database.DB_NAME, "r",) as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt", "a", encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except: 
        print("Database ERROR!")
        
    os.rename("data_temp.txt", Database.DB_NAME)