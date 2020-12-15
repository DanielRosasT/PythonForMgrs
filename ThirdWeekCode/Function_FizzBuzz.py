# FizzBuzz Challenge
# by Daniel Rosas T



#     if counter % 3 == 0 and counter % 5 != 0:
#         print ("Fizz")
#     elif counter % 5 ==  0 and counter % 3 != 0:
#         print ("Buzz")
#     elif counter % 3 == 0 and counter % 5 == 0:
#         print ("FizzBuzz")
# #    elif counter % 3 != 0 and counter % 5 != 0:
#     else:
#         print(counter)
# -------- FizzBUzz using function
# definición de la función
def is_divisable(number, divisor):
    if number % divisor == 0:       
        return True
    else:
        return False
#------------ . --------------------
for counter in range (1,101):
    if is_divisable (counter,3) and is_divisable(counter,5):
        print("FizzBuzz")
    elif is_divisable(counter,3):
        print("Fizz")
    elif is_divisable(counter,5):
        print ("Buzz")
    else:
        print(counter)
