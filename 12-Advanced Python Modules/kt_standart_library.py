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