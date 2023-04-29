# POSITION_HOLDER = '[name]'
#
#
# with open("./Input/Names/invited_names.txt") as invited_name:
#     list_invited_name = invited_name.readlines()
#
# with open("./Input/Letters/starting_letter.txt") as starting_letter:
#     read_starting_letter = starting_letter.read()
#     for new_name in list_invited_name:
#         strip_name = new_name.strip()
#         create_new_letter_with_mew_name = read_starting_letter.replace(POSITION_HOLDER, strip_name)
#         with open(f"./Output/ReadyToSend/letter_for_{strip_name}", mode='w') as new_ready_letter:
#             new_ready_letter = new_ready_letter.write(create_new_letter_with_mew_name)
#
#             print(strip_name)
#
POSITION = "[name]"
with open("./Input/Names/invited_names.txt") as name:
    names = name.readlines()


with open("./Input/Letters/starting_letter.txt") as letter:
    letters = letter.read()
    for one_person in names:
        strip_one_person = one_person.strip()
        new_letters = letters.replace(POSITION, strip_one_person)
        with open(f"./Output/ReadyToSend/letter__{strip_one_person}", mode='w') as new_ready_letter:
            x = new_ready_letter.write(new_letters)