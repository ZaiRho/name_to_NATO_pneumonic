
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("What is your name? ").upper().split()
input_list = [[n for n in item] for item in user_input]
print(input_list)
output = [[data_dict[n] for n in item] for item in input_list]
print(output)
