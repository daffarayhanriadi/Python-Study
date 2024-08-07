from .Operasi import read

def read_console():
    data_file = read()
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
    pass
    