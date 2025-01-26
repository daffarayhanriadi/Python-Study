# TODO-1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(df.to_dict())

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(phonetic_dict)

# TODO-2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)

## Alternative Solution-1
# list_of_phonetic = [p_code for char in word for (letter, p_code) in phonetic_dict.items() if char == letter]
# print(list_of_phonetic)

## Alternative Solution-2
# list_of_phonetic = []

# for char in word:
    # for letter, p_code in phonetic_dict.items():
#         if char == letter:
#             list_of_phonetic.append(p_code)

# print(list_of_phonetic)

