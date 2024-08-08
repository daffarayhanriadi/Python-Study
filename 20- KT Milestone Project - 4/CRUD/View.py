from . import Operasi

def read_console():
    data_file = Operasi.read()
    # print(data_file)
    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"
    
    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {penulis:40} | {judul:40} | {tahun:5}")
    print("-"*100)
    
    # Data
    # print("data")
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {penulis:.40} | {judul:.40} | {tahun:4}", end="")
        
    # Footer
    print("="*100+"\n")
    
def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True:
        try: 
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan lagi (yyyy)")  
        except:
            print("Tahun harus angka, silahkan masukkan lagi (yyyy)")
            
    Operasi.create(penulis, judul, tahun)
    print("\nBerikut adalah data baru anda")
    read_console()

def update_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print("Nomor tidak valid, silahkan masukkan kembali!")
            
    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    while True:
        # Data yang ingin di update
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Penulis\t: {penulis:.40}")
        print(f"2. Judul\t: {judul:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        
        # Memilih mode untuk update
        user_option = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": penulis = input("Penulis\t: ")
            case "2": judul = input("Judul\t: ")
            case "3":
                while True:
                    try: 
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus angka, silahkan masukkan lagi (yyyy)")  
                    except:
                        print("Tahun harus angka, silahkan masukkan lagi (yyyy)")
            case _: print("index tidak cuocuoook")
        
        print("Data baru anda")
        print(f"1. Penulis\t: {penulis:.40}")
        print(f"2. Judul\t: {judul:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah data sudah sesuai (y/n)? ")
        if is_done[0].lower() == "y":
            break
    
    Operasi.update(no_buku, pk, date_add, penulis, judul, tahun)
    
def delete_console():
    read_console()
    while True:
        print("Silahkan pilih nomor buku yang akan di delete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
            
            # Data yang ingin di delete
            print("\n"+"="*100)
            print("Silahkan pilih data yang ingin anda Hapus")
            print(f"1. Penulis\t: {penulis:.40}")
            print(f"2. Judul\t: {judul:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            is_done = input("Apakah anda yakin (y/n)? ")
            if is_done[0].lower() == "y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid, silahkan masukkan kembali!")
            
    print("Data berhasil di hapus")