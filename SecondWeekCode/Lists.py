# In Python there are several ways o grouping
# together things
the_count = [1,2,3,4,5]
stocks = ["FB", "AAPL","NFLX", "GOOG"]
# se pueden poner inclusive una lista dentro de la lista
random_things = [55, 1/2, "puppies", stocks]
# se pueden crear listas vacias
people =[]
# se les pueden adicionar cosas y mantienen el orden
people.append("Mattan")
people.append("Daniel")
people.append("Sam")
print (people)
people.remove("Daniel")
print (people)
# con split se crea una lista, con join se pasa una lista a string
# print ("San Francisco, New York, London".split(", "))
# print(", ".join(["Milk", "Eggs", "Chesse"]))
cities = "San Francisco, New York, London".split(", ")
print(cities)
# se pueden extraer elementos de la lista utilizando []
# la primer posicion de la lista es 0
# la última posicion de la lista es -1
# se pueden traer bloques [0:3] el último no se incluye
first_city = cities[0]
print (first_city)
second_city = cities[1]
print (second_city)
last_city = cities[-1]
print (last_city)
first_two_cities= cities[0:2]
print(first_two_cities)
