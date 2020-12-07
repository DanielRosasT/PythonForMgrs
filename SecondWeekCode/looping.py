#Challenge 2.1 looping program
# by Daniel Rosas
# print out the square of numbers 1 to 100
#
# list_of_numbers =[]
# counter = 1
# while counter <= 100:
#     list_of_numbers.append(counter**2)
#     counter=counter+1
# print (list_of_numbers)

# utilinzado in range
list_of_numbers =[]
for counter in range (1,101):
    print(counter**2)
    list_of_numbers.append(counter**2)
print(list_of_numbers)
