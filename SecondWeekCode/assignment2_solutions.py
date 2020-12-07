# Intro to Programming Using Python - Assignment #2
# Completed by: Mattan Griffel

# 1. Write an if statement that checks if user is "mattangriffel"
# and prints out "Welcome professor" if so, or "Who are you?" if not.

user = "mattangriffel"

if user == "mattangriffel":
    print("Welcome professor!")
else:
    print("Who are you?")


# 2. Write an if statement that checks both the credentials below
# and prints "Successfully logged in." if they're correct or
# "Invalid username/password combination. Try again." if they're not.

user = "mattangriffel"
password = "123456"

if user == "mattangriffel" and password == "123456":
    print("Successfully logged in.")
else:
    print("Invalid username/password combination. Try again.")


# 3. Write an if statement that checks whether the value of number is divisible
# by two and prints out "even" if it is and "odd" if it's not.
# (Hint: You can check divisiblity using the modulus (%) operator. 
# n % k == 0 evaluates to true if n is an exact multiple of k.)

number = 4

if number % 2 == 0:
    print("even")
else:
    print("odd")


# 4. Create three different lists containing:
# - The names of all your siblings
# - Your top 3 favorite movies
# - The latitude and longitude coordinates of Columbia University

siblings = ["Noa", "Marko", "Milan", "Annalin", "Katelin"]
movies = ["Pulp Fiction", "Boyhood", "Magnolia"]
columbia_coordinates = [40.8075, -73.9626]


# 5. Use a for loop on each of the lists above to print out each element on its own line.

for sibling in siblings:
    print(sibling)

for movie in movies:
    print(movie)

for coordinate in columbia_coordinates:
    print(coordinate)


# 6. Use a for loop and the title() function to print out each city name capitalized

cities = ["new york city", "san francisco", "boston", "chicago", "los angeles"]

for city in cities:
    print(city.title())


# 7. A list is different from an element in a list.  What's something you can do
# to the second in Python that you can't do to the first, and vice versa?

person = ["Mattan"]
person = "Mattan"

# - Lists can any hold any type of data i.e. numbers, text, etc, while strings can only hold a set of characters.
# - There are some methods which are common to list and string while various methods are spcific to list and string data type. You can get the full list by using dir().
# - Some examples for strings include "...".upper(), "...".lower(), "...".strip()
# - Some examples for lists include [].append("..."), [].remove("...")


# 8. Use range() and a for loop to print out:
# - the numbers from 1 to 10
# - the square of each of the numbers from 1 to 10
# - for each number from 1 to 10, print out whether it is even or not

for number in range(1, 11):
    print(number)

for number in range(1, 11):
    print(number * number)

for number in range(1, 11):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Bonus: In Mathematics, a Marsenne number is a number that is one less than a
# power of two (i.e. 2^n - 1). Starting with an empty list named 
# marsenne_numbers (provided for you below),  use the append() function inside
# of a for loop so that after the loop has run, marsenne_numbers contains a
# list of the first ten Marsenne numbers.

marsenne_numbers = []
for number in range (1,11):
    marsenne_numbers.append((2**number)-1)
print(marsenne_numbers)

