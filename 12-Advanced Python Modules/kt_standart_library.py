import datetime

time_data = datetime.datetime.now()
print(f"datetime now : {time_data}")
print(f"tahun : {time_data.year}")
print(f"hari : {time_data.strftime('%A')}")

from collections import Counter

data = ["a", "b", "c", "d", "a", "d", "a"]
count_data = Counter(data)

print(f"count data = {count_data}")
print(f"jumlah a = {count_data['a']}")
print(f"jumlah d = {count_data['d']}")

import io 

file = io.open("12-Advanced Python Modules/file_text.txt", "r")
print(file.read())

"""
Output:

datetime now : 2024-08-06 22:53:19.013042
tahun : 2024
hari : Tuesday
count data = Counter({'a': 3, 'd': 2, 'b': 1, 'c': 1})
jumlah a = 3
jumlah d = 2
Say hello from Otong Surotong, makin sekut di mari

"""