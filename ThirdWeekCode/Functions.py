# functions
#
address = ["3022 Broadway, New York, NY 10027, USA",
            "47 W 13th St, New York, NY 10011, USA",
            "70 Washington Square South, New York, NY 10012, United States",
            "777 Brockton Avenue, Abington, MA 2351, USA",
            "70 Pleasant Valley Street, Methuen, MA 1844, USA"]
# city = address.split(", ")[1]
# print (city)
# def get_city(address):
#     return address.split(", ")[1]
def get_state(address):
    return address.split(", ")[2].split()[0]
# print(get_city(address))
for addres in address:
    print(get_state(addres))
