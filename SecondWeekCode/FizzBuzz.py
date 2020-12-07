# FizzBuzz Challenge
# by Daniel Rosas T

for counter in range (1,101):

    if counter % 3 == 0 and counter % 5 != 0:
        print ("Fizz")
    elif counter % 5 ==  0 and counter % 3 != 0:
        print ("Buzz")
    elif counter % 3 == 0 and counter % 5 == 0:
        print ("FizzBuzz")
#    elif counter % 3 != 0 and counter % 5 != 0:
    else:
        print(counter)
