## Challenge Video 1-11 by Daniel Rosas
##
import random

drink = ["Margarita",
        "Bloddy Maryr",
        "Screw DRiver",
        "Red Wine",
        "Corona beer"]

people = ["Henry",
          "guess who",
          "Glenn Hubbard",
          "Samuel L. Jackson",
          "Horn Seng",
          "Peter Gherig"]
counter = 1
while counter < 10:
    random_drink = random.choice(drink)
    random_person = random.choice(people)
    random_person2 = random.choice(people)
    while random_person == random_person2:
        random_person2 = random.choice(people)
    counter = counter+1
    print(f"How about drinking a  {random_drink} with {random_person} and {random_person2}?")

print (f"End of the program with {counter} interactions")
