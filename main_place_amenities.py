#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()



storage.save()


print("OK")