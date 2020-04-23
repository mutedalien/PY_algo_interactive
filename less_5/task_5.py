from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])

# 250

class Person:
    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strenght = strenght

hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)

# 250
# 0.0

New_Person = namedtuple('New_Person', 'name, race, health, mana, strenght')
hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

# 250
# 0.0
# Izverg

print('*' * 50)
Point = namedtuple('Point', 'x, y, z')

p1 = Point(2, z=3, y=4)
print(p1)

# 250
# 0.0
# Izverg
# **************************************************
# Point(x=2, y=4, z=3)

t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

# 250
# 0.0
# Izverg
# **************************************************
# Point(x=2, y=4, z=3)
# Point(x=5, y=10, z=15)

d2 = p2._asdict()
print(d2)

# 250
# 0.0
# Izverg
# **************************************************
# Point(x=2, y=4, z=3)
# Point(x=5, y=10, z=15)
# {'x': 5, 'y': 10, 'z': 15}

p3 = p2._replace(x=6)
print(p3)

# 250
# 0.0
# Izverg
# **************************************************
# Point(x=2, y=4, z=3)
# Point(x=5, y=10, z=15)
# {'x': 5, 'y': 10, 'z': 15}
# Point(x=6, y=10, z=15)

print('*' * 50)
New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0,0])
p4 = New_Point(5)
print(p4)

# 250
# 0.0
# Izverg
# **************************************************
# Point(x=2, y=4, z=3)
# Point(x=5, y=10, z=15)
# {'x': 5, 'y': 10, 'z': 15}
# Point(x=6, y=10, z=15)
# **************************************************
# New_Point(x=5, y=0, z=0)

print(p4._field_defaults)

# 250
# 0.0
# Izverg
# **************************************************
# Point(x=2, y=4, z=3)
# Point(x=5, y=10, z=15)
# {'x': 5, 'y': 10, 'z': 15}
# Point(x=6, y=10, z=15)
# **************************************************
# New_Point(x=5, y=0, z=0)
# {'y': 0, 'z': 0}

dict = {'x': 10, 'y': 20, 'z': 30}
p5 = New_Point(**dict)
print(p5)

# 250
# 0.0
# Izverg
# **************************************************
# Point(x=2, y=4, z=3)
# Point(x=5, y=10, z=15)
# {'x': 5, 'y': 10, 'z': 15}
# Point(x=6, y=10, z=15)
# **************************************************
# New_Point(x=5, y=0, z=0)
# {'y': 0, 'z': 0}
# New_Point(x=10, y=20, z=30)