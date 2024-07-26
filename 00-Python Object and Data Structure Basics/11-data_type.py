# a = 10, a adalah variabel dengan nilai 10
# Cara melakukan compile di python --> python -m py_compile <file_name>

# Tipe data: angka satuan yang tidak ada koma nya (integer)
data_integer = 11
print("data : ", data_integer)
print("- bertipe", type(data_integer))

# Tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe", type(data_float))

# Tipe data: kumpulan karakter (string)
data_string = "kapal lawd"
print("data : ", data_string)
print("- bertipe", type(data_string))

# Tipe data: biner true/false (boolean)
data_bool = False
print("data : ", data_bool)
print("- bertipe", type(data_bool))

## Tipe data khusus

# Bilangan Kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe", type(data_complex))

# tipe data dari bahasa C karena python terbuat dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe", type(data_c_double))

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
data :  (5+6j)
- bertipe <class 'complex'>
data :  c_double(10.5)
- bertipe <class 'ctypes.c_double'>

"""