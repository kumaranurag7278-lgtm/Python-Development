#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"
# make a list of names by importing from Name folder
with open("./Input/Names/invited_names.txt") as new_file:
    names = new_file.readlines()

with open("./Input/Letters/starting_letter.txt") as sample_letter:
    sample = sample_letter.read()
    for name in names:
        srtipped_name = name.strip()
        new_letter = sample.replace(PLACEHOLDER,srtipped_name)

        with open(f"./Output/ReadyToSend/letter_for_{srtipped_name}.docx",'w') as final_letter:
            letter = final_letter.write(new_letter)


          