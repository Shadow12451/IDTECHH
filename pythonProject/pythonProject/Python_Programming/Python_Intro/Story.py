# Create a mad lib story

# Declare Variables
mythicalAnimal = "dragon"
characterName = "Shadow"
age = 1000
secondCharacterName = "Mr. Jorts"
secondCharacterJob = "Teacher"
thirdCharacterName = "Arduino"
place1 = "Cave"
place2 = "IdTech"
pluralNoun1 = "People"
pluralNoun2 = "Buildings"
action = "Seduce"
adj1 = "Dumb"
adj2 = "Perfect"
pastTenseVerb1 = "ate"
pastTenseVerb2 = "sounded"
char = 'a'

# Create the story
Incorrect = "Password Incorrect, try again."
story = "Once upon " + char + " time, there was " + char + " " + adj1 + " " + mythicalAnimal + " named " + \
        characterName + ". " + characterName + " was " + char + " " + str(age) + " years old and lived by the " + \
        place1 + ". He " + pastTenseVerb1 + " " + pluralNoun1 + " and " + pluralNoun2 + ". People thought " + \
        characterName + " was too " + adj1 + ". The people sent " + secondCharacterName + ", the village's " \
        + secondCharacterJob + ", to " + action + " the " + mythicalAnimal + ". " + characterName + " thought that " \
        + pastTenseVerb2 + " " + adj2 + ", so he left the " + place1 + ". Now he lives in the " + place2 \
        + " and eats the " + pluralNoun1 + " and " + pluralNoun2 + " there instead." + " but the " + mythicalAnimal + " started to feel sad " + " so " + thirdCharacterName + " started a fight with " + secondCharacterName + "," + " after winning the fight, " +  thirdCharacterName + " started dancing on " + secondCharacterName + " then he " + " married the " + mythicalAnimal + " and lived happily ever after "
password = input("Enter the password: ")
if password == "PythonCoding":
        print(story)
else: print(Incorrect)