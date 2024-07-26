# a = 10, a adalah variabel dengan nilai 10
# Cara melakukan compile di python --> python -m py_compile <file_name>

## Tipe Data Dasar

# Integer (int): Menyimpan bilangan bulat.
data_integer = 11
print("data : ", data_integer)
print("- bertipe", type(data_integer))

# Float (float): Menyimpan bilangan desimal.
data_float = 1.5
print("data : ", data_float)
print("- bertipe", type(data_float))

# String (str): Menyimpan teks.
data_string = "kapal lawd"
print("data : ", data_string)
print("- bertipe", type(data_string))

# Boolean (bool): Menyimpan nilai benar (True) atau salah (False).
data_bool = False
print("data : ", data_bool)
print("- bertipe", type(data_bool))

# NoneType: Tipe data untuk menyatakan nilai yang tidak ada atau null.
data_none = None
print("data : ", data_none)
print("- bertipe", type(data_none))

## Tipe Data Koleksi

# List: Koleksi yang terurut dan dapat diubah (mutable). Dapat menyimpan berbagai tipe data.
data_list = ["apple", "banana", "cherry"]
print("data : ", data_list)
print("- bertipe", type(data_list))

# Tuple: Koleksi yang terurut dan tidak dapat diubah (immutable). Dapat menyimpan berbagai tipe data.
data_tuple = (10.0, 20.0)
print("data : ", data_tuple)
print("- bertipe", type(data_tuple))

# Dictionary (dict): Koleksi pasangan kunci-nilai (key-value pairs) yang tidak terurut.
data_dict = {"name": "Alice", "age": 30}
print("data : ", data_dict)
print("- bertipe", type(data_dict))

# Set: Koleksi yang tidak terurut dan tidak mengizinkan duplikasi.
data_set = {1, 2, 3, 4, 5}
print("data : ", data_set)
print("- bertipe", type(data_set))

# FrozenSet: Versi set yang tidak dapat diubah (immutable).
data_forzenset = frozenset([1, 2, 3, 4, 5])
print("data : ", data_forzenset)
print("- bertipe", type(data_forzenset))

## Tipe Data Khusus

# Bytes: Menyimpan urutan byte (tidak dapat diubah).
data_byte = b"hello"
print("data : ", data_byte)
print("- bertipe", type(data_byte))

# Bytearray: Menyimpan urutan byte (dapat diubah).
data_bytearray = bytearray(b"hello")
print("data : ", data_bytearray)
print("- bertipe", type(data_bytearray))

# Memoryview: Memberikan tampilan langsung ke data buffer yang dapat diubah tanpa menyalin.
data_memoryview = memoryview(data_bytearray)
print("data : ", data_memoryview)
print("- bertipe", type(data_memoryview))

## Tipe Data Lainnya

# Bilangan Kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe", type(data_complex))

# Tipe data dari bahasa C karena python terbuat dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe", type(data_c_double))

### Masih banyak tipe data lainnya (Advance)

"""
Output:

data :  11
- bertipe <class 'int'>
data :  1.5
- bertipe <class 'float'>
data :  kapal lawd
- bertipe <class 'str'>
data :  False
- bertipe <class 'bool'>
data :  None
- bertipe <class 'NoneType'>
data :  ['apple', 'banana', 'cherry']
- bertipe <class 'list'>
data :  (10.0, 20.0)
- bertipe <class 'tuple'>
data :  {'name': 'Alice', 'age': 30}
- bertipe <class 'dict'>
data :  {1, 2, 3, 4, 5}
- bertipe <class 'set'>
data :  frozenset({1, 2, 3, 4, 5})
- bertipe <class 'frozenset'>
data :  b'hello'
- bertipe <class 'bytes'>
data :  bytearray(b'hello')
- bertipe <class 'bytearray'>
data :  <memory at 0x000001A67AD04E80>
- bertipe <class 'memoryview'>
data :  (5+6j)
- bertipe <class 'complex'>
data :  c_double(10.5)
- bertipe <class 'ctypes.c_double'>

"""