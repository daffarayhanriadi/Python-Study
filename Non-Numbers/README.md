## String

String adalah urutan dari karakter unicode yang dideklarasikan dengan petik tunggal atau ganda. Element String bersifat immutable, sehingga tidak dapat dilakukan perubahan element menggunakan metode slicing. Namun kita dapat melakukan perubahan pada string secara utuh.

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