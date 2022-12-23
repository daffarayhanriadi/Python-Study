# Setiap data di dalamnya dapat diakses dengan indeks yang dimulai dari 0.
a = [1, 2.2, 'python']

print(a)

# Mengakses data pada list
x = [5, 10, 15, 20, 25, 30, 35, 40]
print('\n==Output Slicing Element List==')
print(x[0])
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:7:2])

# Mengubah elemen pada list
print('\n==Output Update Element List==')
x = [1, 2, 3]
x[2] = 4
print(x)

# Menambah elemen pada list menggunakan fungsi append()
print('\n==Output Add Element List==')
x = [1, 2, 3]
x[2] = 4
x.append(5)
print(x)

# Menghapus elemen pada list menggunakan fungsi del
binatang = ['kucing', 'rusa', 'badak', 'gajah']
del binatang[2]
print('\n==Output Delete Element List==')
print(binatang)

del binatang[2]
print('\n{}'.format(binatang))
