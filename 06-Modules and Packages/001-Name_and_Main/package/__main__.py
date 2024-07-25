"""

Jika file __main__.py berada di dalam sebuah package, 
fungsi utamanya adalah untuk menentukan titik masuk utama 
ketika package tersebut dijalankan sebagai sebuah skrip. 
Dengan kata lain, __main__.py memungkinkan package dijalankan 
langsung dengan menggunakan perintah python -m <nama_package>.

Fungsi dan Manfaat __main__.py dalam Package
1. Titik Masuk Utama:
    * File __main__.py berfungsi sebagai titik masuk utama untuk 
      package. Ketika kita menjalankan package dengan perintah 
      python -m <nama_package>, Python akan mencari dan 
      mengeksekusi __main__.py.

2. Memungkinkan Eksekusi Package:
    * Dengan adanya __main__.py, kita dapat menjalankan seluruh 
      package seolah-olah package tersebut adalah skrip tunggal. 
      Ini sangat berguna untuk package yang dirancang untuk 
      dieksekusi langsung, seperti aplikasi command-line atau 
      skrip utilitas.

3. Struktur Kode yang Rapi:
    * __main__.py memungkinkan kita untuk menjaga struktur kode 
      yang rapi dengan memisahkan logika eksekusi dari logika 
      fungsional. Kode eksekusi ditempatkan dalam __main__.py, 
      sementara fungsi dan kelas dapat ditempatkan dalam 
      modul-modul lain dalam package.

"""

# __main__ ini digunakan sebagai dokumentasi

print("ini adalah main dari package")
print()
print(f"")