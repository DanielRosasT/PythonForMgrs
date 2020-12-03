import random

bars = ["The Hamilton",
        "1020 Bar",
        "The Heights",
        "The Dead Poet",
        "Cantina y Punto"]

people = ["Mattan",
          "that person you forgot to text back",
          "Glenn Hubbard",
          "Samuel L. Jackson",
          "Horn Seng",
          "Peter Gherig"]
counter = 1
while counter < 10:
    random_bar = random.choice(bars)
    random_person = random.choice(people)
    random_person2 = random.choice(people)
    while random_person == random_person2:
        random_person2 = random.choice(people)
    counter = counter+1
    print(f"How about you go to {random_bar} with {random_person} and {random_person2}?")

print (f"End of the program with {counter} interactions")
