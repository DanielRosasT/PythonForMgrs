# Intro to Programming Using Python - Assignment #1
# Completed by: Daniel Rosas

# 1. Print out the following text:
# You've reached [your name].
# I'm not available right now, so leave a message and I'll call you back.
my_name = "Daniel"
print(f"\n\nYou\'ve reached {my_name}.")
print ("I\'m not available right now, so leave a message and I\'ll call you back")

# 2. Create five variables for your first name, last name, shoe size, height, and age.
# And then print them out on one line.
first_name = "Daniel"
last_name = "Rosas"
shoe_size = 40
height_mts = 1.77
age_years = 60

print(f"My nanme is {first_name} {last_name} my shoe size is \
{shoe_size}, height {height_mts} mts. and age {age_years}")

# 3. If subtotal = 10.58 and tip = 0.22 (22%) then calculate the total bill amount
# in a variable named total and print it out.
subtotal = 10.58
tip = 0.22
total = subtotal + (subtotal*tip)
print (f"${total:.2f}")

# 4. Convert 158.8 into an integer.
# Convert 75 into a float.
# Convert "244.9" into a float and then an integer.
print(float (75),int(244.9))
int(float("244.9"))

# 5. Use \t and \n in a string and then print it out so that it matches (approximately) the following:
# -in the woods
#               which
#                   stutter
#                           and
#
#                               sing
print("-in the woods\n\t\twhich\n\t\t\tstutter\n\t\t\t\tand\n\t\t\t\t\tsing\n")


# 6. Put your first name and total from above into an f-string (f"...") so that it reads:
# Mattan, your total is $12.91
# (remember to round the total to the nearest cent)
print(f"{first_name} your total is ${total:.2f}\n")

# 7. Use input() to ask a user for the city they live in, and then print it back to them.
city_wil = input("in which city you are living in? ")
print (f"{first_name} is living in {city_wil}\n")

# 8. Build a future value calculator by using input() to get values from the user.
# (Make sure you convert them into integers or floats before doing any math on them.)
# Print out the result.
# Hint: Future Value = Present Value x (1 + rate of return) ^ number of periods

present_value = float(input("please introduce present value: "))
rate_of_return= float(input("please introduce the return rate % "))
number_of_periods = float(input("please introduce the number of periods: "))
future_value = present_value*(1+rate_of_return/100)**number_of_periods
print (f"future value ${future_value:.2f}")

print ("\n\t--end of the assignment 1 --\n")
