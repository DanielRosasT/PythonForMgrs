# Tercer semana diccionarios
#los diccionarios agregarn nombres a
#las psociiones de una lista, para definirlo
# se usan los corchetes parentesis {}
# ejemplo
stock = {"name": "Daniel Rosas",
        "Height": 1.77,
        "Shoe Size":42,
        "Hair":"Brown",
        "Eye Color": "Green"}

print (f"nombre: {stock['name']}, Height: {stock['Height']},\
 Shoe Size: {stock['Shoe Size']}, Hair: {stock['Hair']},\
 Eye Color: {stock['Eye Color']}")

stock["open price"]  = 100.25
stock["close price"] = 106.03

print(stock)
movies = "Matrix, Amores perros, Roma"
# split converts a string into a list
stock["favourite movies"]= movies.split(", ")
print(stock["favourite movies"])
# join converts a list into a string
print(", ".join(stock["favourite movies"]))
