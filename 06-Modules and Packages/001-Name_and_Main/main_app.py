"""
Apa itu if __name__ == "__main__":?
Ketika Anda menjalankan skrip Python, interpreter menetapkan nilai 
ke variabel khusus __name__. Nilai ini bisa berbeda tergantung 
pada bagaimana skrip dijalankan.

1. Ketika Anda Menjalankan Skrip Secara Langsung:
    * Jika Anda menjalankan skrip secara langsung menggunakan 
    perintah python myscript.py, nilai __name__ akan menjadi 
    "__main__".
2. Ketika Skrip Diimpor sebagai Modul:
    * Jika skrip diimpor ke skrip lain, nilai __name__ akan 
    menjadi nama dari modul tersebut.

if __name__ == "__main__" pada Python memungkinkan kita untuk 
menentukan baris tertentu manakah yang akan dijalankan ketika 
script berbentuk file kita jalankan, tapi tidak ketika fungsi 
tersebut diimport dalam bentuk module ke dalam file script lain.

Mengapa Ini Berguna?
Ini berguna untuk memisahkan kode yang hanya perlu dijalankan 
ketika skrip dijalankan secara langsung dari kode yang harus 
tersedia ketika skrip diimpor sebagai modul.
"""

# __main__ adalah top level code environment (__nama__)

# __name__ == "__main__" akan terjadi jika ada di file program utama

## __name__ pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

## __name__ pada file program eksternal
import fungsi

## contoh penggunaan __main__

# deklarasi
def funsi_tambah(a:int, b:int) -> int:
    return a + b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = funsi_tambah(angka1, angka2)
    print(f"hasil tambah = {hasil}")
    
## import package
import package # tidak ada output, 