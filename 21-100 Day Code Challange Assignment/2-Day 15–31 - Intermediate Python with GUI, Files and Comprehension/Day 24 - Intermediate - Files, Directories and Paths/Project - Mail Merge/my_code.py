# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Names/invited_names.txt", "r") as invited_names_file:
    invited_names = invited_names_file.readlines()
    for name in invited_names:
        name = name.strip("\n")
        with open("./Input/Letters/starting_letter.txt", "r") as letter_file:
            letter_sentences = letter_file.readlines()
            for sentence in letter_sentences:
                with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "a") as output_file:
                    output_file.write(f"{sentence.replace("[name]", name)}")
