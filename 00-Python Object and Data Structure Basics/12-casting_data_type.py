# Merubah dari satu tipe data ke tipe data lain

## INTEGER
print("====INTEGER====")
data_int = 9
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # Akan False jika nilai int = 0
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 9.9
print("data = ", data_float, ",type = ", type(data_float))

data_int = int(data_float) # Akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # Akan False jika nilai float = 0.0
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_bool, ",type = ", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_boolean = False
print("data = ", data_boolean, ",type = ", type(data_boolean))

data_int = int(data_boolean)
data_str = str(data_boolean)
data_float = float(data_boolean)
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_str, ",type = ", type(data_str))
print("data = ", data_float, ",type = ", type(data_float))

## STRING
print("====STRING====")
# data_str = "kapal lawd" # Error kalau di cast ke angka
data_str = "10"
print("data = ", data_str, ",type = ", type(data_str))

data_int = int(data_str) # String harus angka
data_float = float(data_str) # String harus angka
data_bool = bool(data_str) # False jika STRING kosong
print("data = ", data_int, ",type = ", type(data_int))
print("data = ", data_float, ",type = ", type(data_float))
print("data = ", data_bool, ",type = ", type(data_bool))

"""
Output:

====INTEGER====
data =  9 ,type =  <class 'int'>
data =  9.0 ,type =  <class 'float'>
data =  9 ,type =  <class 'str'>
data =  True ,type =  <class 'bool'>
====FLOAT====
data =  9.9 ,type =  <class 'float'>
data =  9 ,type =  <class 'int'>
data =  9.9 ,type =  <class 'str'>
data =  True ,type =  <class 'bool'>
====BOOLEAN====
data =  False ,type =  <class 'bool'>
data =  0 ,type =  <class 'int'>
data =  False ,type =  <class 'str'>
data =  0.0 ,type =  <class 'float'>
====STRING====
data =  10 ,type =  <class 'str'>
data =  10 ,type =  <class 'int'>
data =  10.0 ,type =  <class 'float'>
data =  True ,type =  <class 'bool'>

"""
