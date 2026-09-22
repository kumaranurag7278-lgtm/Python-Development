import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv") 
    

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index,row) in data.iterrows()}
# print(nato_dict)



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word").upper()
def generate_phonetic():
    try:
        output_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Bitch can you please type a word")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()