"""

Ada tiga metode pada class tersebut yang semua namanya diawali dengan kata test. 
Hal ini merupakan konvensi (aturan) yang wajib diikuti untuk menginformasikan ke test runner bahwa 
sejumlah metode tersebut merepresentasikan tes yang akan dioperasikan.

Mengapa Menggunakan if __name__ == '__main__':
1. Memungkinkan Pengujian Langsung:
    * Saat Anda menjalankan skrip pengujian secara langsung, blok kode ini memastikan bahwa 
      unittest.main() dipanggil dan semua pengujian dijalankan.
2. Memisahkan Pengujian dari Impor:
    * Jika Anda mengimpor skrip pengujian ke dalam modul lain (misalnya untuk menjalankan pengujian 
      secara otomatis sebagai bagian dari suite pengujian yang lebih besar), Anda tidak ingin 
      unittest.main() dijalankan secara otomatis. Blok if __name__ == '__main__': mencegah hal ini 
      terjadi.
3. Fleksibilitas dan Keterbacaan:
    * Dengan memisahkan logika eksekusi pengujian ke dalam blok ini, skrip pengujian Anda menjadi 
      lebih fleksibel dan mudah dibaca. Ini memungkinkan kode pengujian digunakan kembali dalam 
      konteks lain tanpa eksekusi pengujian langsung yang tidak disengaja.

Mengapa Menggunakan unittest.main()?
1. Otomatisasi Pengujian:
    * unittest.main() mengotomatiskan proses menemukan dan menjalankan pengujian, sehingga Anda tidak 
      perlu secara manual memanggil setiap metode pengujian.
2. Standar dan Praktik Terbaik:
    * Menggunakan unittest.main() adalah praktik standar dalam menulis pengujian unit di Python. 
      Ini memastikan bahwa skrip pengujian Anda mengikuti konvensi yang diakui dan dapat dengan mudah 
      dipahami oleh pengembang lain.
3. Kemudahan Eksekusi:
    * Dengan unittest.main(), Anda cukup menjalankan skrip pengujian dari baris perintah tanpa harus 
      menulis kode tambahan untuk menginisialisasi dan menjalankan pengujian.
4. Fleksibilitas:
    * Fungsi ini juga mendukung berbagai opsi dan fitur, seperti menjalankan pengujian tertentu saja, 
      mengubah output, dan integrasi dengan sistem pengujian kontinu.
      
Tujuan unittest.main()
Fungsi unittest.main() melakukan tugas berikut:
1. Menemukan dan menjalankan semua metode pengujian yang ada dalam kelas pengujian yang ditentukan 
   (TestCap dalam contoh ini).
2. Menyediakan antarmuka baris perintah untuk menjalankan pengujian, yang memungkinkan hasil 
   pengujian dicetak ke konsol.

"""

import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
    def test_with_apostrophes(self):
        text = "monty python's flying circus"
        result = cap.cap_text(text)
        self.assertEqual(result, "Monty Python's Flying Circus")
        
if __name__ == '__main__':
    unittest.main()