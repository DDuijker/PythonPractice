# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt', 'r') as names:
    for name in names:
        name = name.strip("\n")
        # Replace the [name] in starting letter with the name
        with open('./Input/Letters/starting_letter.txt', mode='r') as letter_content:
            letter = letter_content.read().replace(PLACEHOLDER, name)

            # Save new letter
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as invite:
                invite.write(letter)

