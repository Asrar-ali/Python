PLACEHOLDER = "[name]"
##to open the text file
with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

##
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completer_letter:
            completer_letter.write(new_letter)
