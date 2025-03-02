with open("./Input/Letters/starting_letter.txt","r") as file:
    text=file.read()
with open("./Input/Names/invited_names.txt") as file:
    names=file.readlines()
for i in range(len(names)):
    name=names[i].strip("\n")
    ntext=text.replace("[name]",name)
    print(ntext)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt","w") as file:
        file.write(ntext)
