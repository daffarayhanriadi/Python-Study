s1 = "Ini adalah string baris tunggal"

s2 = '''Ini adalah string
yang memiliki baris pertama
dan selanjutnya baris kedua'''

print(s1)
print()
print(s2)


# Slicing pada String
s = "Hello World!"
print('\n==Output Slicing String==')
print(s[4])  # ambil karakter kelima dari string s
print(s[6:11])  # ambil karakter ketujuh hingga sebelas dari string s
# s[5] = "d"  # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
print(s)

# Ubah secara utuh String
s = "Hello World!"
s = "Halo Dunia!" # ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print('\n==Output Update String==')
print(s)
