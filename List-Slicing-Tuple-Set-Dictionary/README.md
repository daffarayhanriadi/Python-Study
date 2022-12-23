# List-Slicing-Tuple-Set-Dictionary

## List
List adalah jenis kumpulan data terurut (ordered sequence). List pada Python tidak harus memiliki tipe data yang sama. Diakses dengan indeks yang dimulai dari 0. List didefinisikan dengan kurung siku **[]** dan elemen yang dipisahkan dengan koma.

* **x[0]** artinya mengambil elemen paling awal, dengan index 0 dari List x.
* **x[5]** artinya mengambil elemen dengan index 5 dari List x.
* **x[-1]** artinya mengambil elemen dengan index paling belakang ke-1 dari List x.
* **x[3:5]** artinya membuat list dari anggota elemen List x dengan index 3 hingga sebelum index 5 (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 3-4).
* **x[:5]** artinya membuat list dari anggota elemen List x paling awal hingga sebelum index 5 (tidak termasuk elemen dengan index 5, dalam hal ini hanya index 0-4).
* **x[-3:]** artinya membuat list dari anggota elemen List x mulai index ke-3 dari belakang hingga paling belakang.
* **x[1:7:2]** artinya membuat list dari anggota elemen List x dengan index 1 hingga sebelum index 7, dengan "step" 2 (dalam hal ini hanya index 1, 3, 5).

---

## Slicing

---

## Tuple

Tuple adalah jenis dari list yang tidak dapat diubah elemennya. Umumnya digunakan untuk data yang bersifat sekali tulis, dan dapat dieksekusi lebih cepat. Tuple didefinisikan dengan kurung **()** dan elemen yang dipisahkan dengan koma.

---

## Set

Set adalah kumpulan item bersifat unik dan tanpa urutan (unordered collection). Didefinisikan dengan kurawal **{}** dan elemennya dipisahkan dengan koma. Pada Set kita dapat melakukan union dan intersection, sekaligus otomatis melakukan penghapusan data duplikat.

---

## Dictionary

Dictionary pada Python adalah kumpulan pasangan kunci-nilai (pair of key-value) yang bersifat tidak berurutan. Dictionary dapat digunakan untuk menyimpan data kecil hingga besar. Untuk mengakses datanya, kita harus mengetahui kuncinya (key). Pada Python, dictionary didefinisikan dengan kurawal dan tambahan definisi berikut:

* Setiap elemen pair key-value dipisahkan dengan koma (,).
* Key dan Value dipisahkan dengan titik dua (:).
* Key dan Value dapat berupa tipe variabel/obyek apapun.

Dictionary bukan termasuk dalam implementasi urutan (sequences), sehingga tidak bisa dipanggil dengan urutan indeks.