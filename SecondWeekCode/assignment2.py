# Intro to Programming Using Python - Assignment #2
# Completed by: Daniel Rosas

# 1. Write an if statement that checks if user is "mattangriffel"
# and prints out "Welcome professor" if so, or "Who are you?" if not.

user = input("username: ? ")
if user.lower() == "mattangriffel" :
    print ("Welcome professor")
else:
    print ("who are you")



# 2. Write an if statement that checks both the credentials below
# and prints "Successfully logged in." if they're correct or
# "Invalid username/password combination. Try again." if they're not.

user = input("username: ? ") #"mattangriffel"
password = input("password: ? ") #"123456"
if user.lower() == "mattangriffel" and password == "123456":
    print("succesfully logged in !")
else:
    print("Invalid username/password combination. Try again." )

# 3. Write an if statement that checks whether the value of number is divisible
# by two and prints out "even" if it is and "odd" if it's not.
# (Hint: You can check divisiblity using the modulus (%) operator.
# n % k == 0 evaluates to true if n is an exact multiple of k.)

number = float(input("Type a number: "))
if number % 2 == 0:
    print ("even")
else:
    print("odd")



# 4. Create three different lists containing:
# - The names of all your siblings
# - Your top 3 favorite movies
# - The latitude and longitude coordinates of Columbia University

siblings =["Mario", "Adriana", "Elizabeth", "Marco Antonio", "Guadalupe"]
Fav_movies = ["Matrix", "Amores perros", "Roma"]
Columbia_coordinates = ["latitude: ", "40° 48' 16.19\" N", "Longitude: ", "-73° 57' 25.79\" W"]
# 5. Use a for loop on each of the lists above to print out each element on its own line.

for sibling in siblings:
    print (sibling)
for Fav_movie in Fav_movies:
    print (Fav_movie)
for Columbia_coordinate in Columbia_coordinates:
    print (Columbia_coordinate)

# 6. Use a for loop and the title() function to print out each city name capitalized

cities = ["new york city", "san francisco", "boston", "chicago", "los angeles"]
for city in cities:
    print(city.title())


# 7. A list is different from an element in a list.  What's something you can do
# to the second in Python that you can't do to the first, and vice versa?

person = ["Mattan"] # I can append or remove elements and can turn it into a str
person = "Mattan"   # I can turn it into a list


# 8. Use range() and a for loop to print out:
# - the numbers from 1 to 10
# - the square of each of the numbers from 1 to 10
# - for each number from 1 to 10, print out whether it is even or not
for numbers in range (1,11):
    print(numbers)

    print("square ", numbers**2)

    if numbers % 2 == 0:
        print ("even")
    else:
        print ("odd")

# Bonus: In Mathematics, a Marsenne number is a number that is one less than a
# power of two (i.e. 2^n - 1). Starting with an empty list named
# marsenne_numbers (provided for you below),  use the append() function inside
# of a for loop so that after the loop has run, marsenne_numbers contains a
# list of the first ten Marsenne numbers.

marsenne_numbers = []
for i in range (1,11):
    marsenne_numbers.append(2**i-1)
print(marsenne_numbers)
