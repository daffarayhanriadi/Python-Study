# Membuat gabungan area rentang dari angka


inputUser = int(input("Masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n: "))

# ++++++3--------------
# Memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)


# --------------10++++++
# Memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# ++++++3------10++++++
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan :", isCorrect)

print("\n", "="*10, "\n")

# Ini adalah kasus irisan
inputUser = int(input("Masukkan angka yang bernilai \nlebih dari 3 \ndan \nkurang dari 10\n: "))

# ------3++++++++++++++
# lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 :", isLebihDari)

# +++++++++++++10------
isKurangDari = (inputUser < 10)
print("Kurang dari 10 :", isKurangDari)

# ------3++++++10------
isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan :", isCorrect)

print("\n", "="*10, "\n")

# PR
# 1. ------0++++++5------8++++++11------ input > 0 and input < 5 or input > 8 and input < 11
# 2. ++++++0------5++++++8------11++++++ input < 0 or input > 5 and input < 8 or input > 11

inputUser = int(input("Masukkan angka yang bernilai \nlebih dari 0 \ndan \nkurang dari 5\natau \nlebih dari 8 \ndan \n kurang dari 11\n: "))

# ------0++++++
isLebihDari0 = (inputUser > 0)
print("Lebih dari 0 :", isLebihDari0)

# ++++++5------
isKurangDari5 = (inputUser < 5)
print("Kurang dari 5 :", isKurangDari5)

# ------8++++++
isLebihDari8 = (inputUser > 8)
print("Lebih dari 8 :", isLebihDari8)

# ++++++11------
isKurangDari11 = (inputUser < 11)
print("Kurang dari 11 :", isKurangDari11)

# ------0++++++5------8++++++11------
isCorrect = isKurangDari5 and isLebihDari0 or isKurangDari11 and isLebihDari8
print("Angka yang anda masukkan :", isCorrect)

print("\n", "="*10, "\n")

inputUser = int(input("Masukkan angka yang bernilai \nkurang dari 0 \natau \nlebih dari 5\ndan \nkurang dari 8 \natau \nlebih dari 11\n: "))

# ++++++0------
isKurangDari0 = (inputUser < 0)
print("Kurang dari 0 :", isKurangDari0)

# ------5++++++
isLebihDari5 = (inputUser > 5)
print("Lebih dari 5 :", isLebihDari5)

# ++++++8------
isKurangDari8 = (inputUser < 8)
print("Kurang dari 8 :", isKurangDari8)

# ------11++++++
isLebihDari11 = (inputUser > 11)
print("Lebih dari 11 :", isLebihDari11)

# ++++++0------5++++++8------11++++++
isCorrect = isKurangDari and isLebihDari or isKurangDari and isLebihDari
print("Angka yang anda masukkan :", isCorrect)