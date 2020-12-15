# list of dictionaries
mattan = {'name': 'Mattan',
          'height': 70,
          'shoe size': 10.5,
          'hair': 'Brown',
          'eyes': 'Brown',
          'favorite movies': ['Pulp Fiction',
                              'Magnolia',
                              'The Royal Tenenbaums']}

chris =  {'name': 'Chris',
          'height': 72,
          'shoe size': 11,
          'hair': 'Blonde',
          'eyes': 'Blue',
          'favorite movies': ['Shawshank Redemption',
                              'Lord of the Rings']}

lisa =   {'name': 'Lisa',
          'height': 64,
          'shoe size': 6.5,
          'hair': 'Black',
          'eyes': 'Brown',
          'favorite movies': ['Crazy Rich Asians',
                              'Avengers',
                              'Lord of the Rings']}

daniel = {"name": "Daniel",
        "height": 69,
        "shoe size":7,
        "hair":"Brown",
        "eyes": "Green",
        'favorite movies': ['Matrix',
                            'Amores perros',
                            'Roma']}

users = [mattan,chris,lisa,daniel]
brown_eyes_users = []
for user in users:
# print (f"{user['name']}\'s shoe size is {user['shoe size']}")
 #selecting a subset of users
    if user['eyes'] == "Brown":
        brown_eyes_users.append(user)

print (brown_eyes_users)
