# Numbers

Tipe numerik pada Python dibagi menjadi 3 bagian: int, float dan complex.

---

## Integer

Integer tidak dibatasi oleh angka atau panjang tertentu, namun dibatasi oleh memori yang tersedia.

---

## Batasan akurasi variabel bertipe float

Python melakukan pemotongan pada digit ke 16 dari variabel float. Sehingga hanya dapat menampilkan sampai 15 digit desimal saja.

---

## Complex

Karena Python banyak digunakan oleh matematikawan, tipe bilangan di Python juga mendukung bilangan imajiner dan bilangan kompleks. Nilai bilangan kompleks (complex) dituliskan dalam formulasi x + yj, yakni bagian x adalah bilangan real dan y adalah bilangan imajiner.

---

## String

String adalah urutan dari karakter unicode yang dideklarasikan dengan petik tunggal atau ganda.

---

## Boolean

**False dan True.**

Ada fungsi bawaan bool() yang dapat mengubah nilai menjadi nilai Boolean, apabila nilai tersebut dapat direpresentasikan sebagai nilai kebenaran (truth values). 

Nilai kebenaran adalah sebuah nilai yang dapat diuji sebagai benar atau salah, untuk digunakan di sintaksis kondisi if atau while atau sebagai operan dari operasi Boolean.

Berikut adalah objek bawaan yang didefinisikan bernilai salah dalam pengujian nilai kebenaran:

* Konstanta yang sudah didefinisikan bernilai salah: None dan False.
* Angka nol dari semua tipe numeric: 0, 0.0, 0j, Decimal(0), Fraction(0, 1).
* Urutan (sequence) dan koleksi (collection) yang kosong: '', (), {}, set(), range(0).

Untuk objek yang didefinisikan sendiri, representasi nilai Boolean akan bergantung dari definisi metode (method) khusus bernama __bool__(self). Jika metode ini mengembalikan True maka interpretasi nilai dari objeknya akan True, demikian juga sebaliknya.