# Testing appending values to a dictionary
steve = {"name":"Steve",
        "homework":[],
        "quizzes":[],
        "tests":[]}
alice = {"name":"Alice",
        "homework":[],
        "quizzes":[],
        "tests":[]}
tyler = {"name":"Tyler",
        "homework":[],
        "quizzes":[],
        "tests":[]}
daniel = {"name":"daniel",
        "homework":[90,97,75,92],
        "quizzes":[],
        "tests":[]}
# 2. Now fill in the dictionaries above with the following scores and print the dictionaries:
# Steve
#   Homework: 90, 97, 75, 92
#   Quizzes: 88, 40, 94
#   Tests: 75, 90
# Alice
#   Homework: 100, 92, 98, 100
#   Quizzes: 82, 83, 91
#   Tests: 89, 97
# Tyler
#   Homework: 0, 87, 75, 22
#   Quizzes: 0, 75, 78
#   Tests: 100, 100
homework_steve = [90,97,75,92]
quizzes_steve = [88,40,94]
tests_steve = [75,90]
#
homework_alice = [100,92,98,100]
quizzes_alice = [82,83,91]
tests_alice = [89,97]
#
homework_tyler = [0,87,75,22]
quizzes_tyler= [0,75,78]
tests_tyler = [100,100]

for notas in homework_steve:
    steve['homework'].append(notas)
for notas in quizzes_steve:
    steve['quizzes'].append(notas)
for notas in tests_steve:
    steve['tests'].append(notas)
#
for notas in homework_alice:
    alice['homework'].append(notas)
for notas in quizzes_alice:
    alice['quizzes'].append(notas)
for notas in tests_alice:
    alice['tests'].append(notas)
#
for notas in homework_tyler:
    tyler['homework'].append(notas)
for notas in quizzes_tyler:
    tyler['quizzes'].append(notas)
for notas in tests_tyler:
    tyler['tests'].append(notas)

print(steve,alice,tyler,daniel)
