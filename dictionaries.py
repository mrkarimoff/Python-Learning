# Dictionaries (looks like JS objects), key/value pairs

person = {"name": "Mirfayz", "age": 25, "occupation": "Software engineer"}

person2 = dict(name="Shoqosim", age=26, occupation="Hater")

name = person["name"]
items = person.items()

# update dict
person.update({"hobby": "Movies"})

# delete and clear
del person["age"]
person.clear()

# copy dictionaries
person = person2  # creates reference `bad copy`
person3 = person.copy()
person4 = dict(person)

# Nested Dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals",
}

member2 = {
    "name": "Page",
    "instrument": "guitar",
}
band = {"member1": member1, "member2": member2}
