list1 = list()   # empty list
x = 5
y = "Leeloo"
list2 = [1, 2, 3, x, y]   # initialized list
print(f"list2: {list2}")
print("list2:", list2)

print(list2[3])
x = 100
print(f"list2: {list2}")
print(list2)
print(repr(list2))
print(str(list2))
list3 = []   # empty list
list4 = list()  

cities = ['Bethesda', 'Columbia', 'Annandale', 'Fairfax', 'College Park']
print(f"cities: {cities}")
print(', '.join(cities))

cities.append('Silver Spring')
cities.insert(0, 'Takoma')
cities.insert(3, 'Gaitherburg')
print(f"cities: {cities}")

more_cities = ['Ellicot City', 'Pasadena', 'Annapolis']
cities.extend(more_cities)
print(f"cities: {cities}")

#  LIST.insert(pos, obj)   LIST.append(obj)   LIST.extend(iterable)

del cities[3]    #  del obj      del LIST[pos]      del DICT[key]
print(f"cities: {cities}")

cities.remove('Fairfax')
print(f"cities: {cities}")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(4)
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]    LIST.remove(value)     LIST.pop()    LIST.pop(pos)

pos = cities.index('Silver Spring')
print(f"pos: {pos}")

cities.sort()   #  cf. sorted(container)
print(f"cities: {cities}")
cities.reverse()   # cf.   reversed(container)
print(f"cities: {cities}")

print(f"cities[0]: {cities[0]}")
print(f"cities[4]: {cities[4]}")
# print(f"cities[19]: {cities[19]}")   # INVALID
print(f"cities[len(cities)-1]: {cities[len(cities)-1]}")
print(f"cities[-1]: {cities[-1]}")
print()
print(f"cities: {cities}")

print(f"cities[1:4]: {cities[1:4]}")
print(f"cities[0:3]: {cities[0:3]}")
print(f"cities[:3]: {cities[:3]}")
print()

print(f"cities[-2:len(cities)]: {cities[-2:len(cities)]}")
print(f"cities[-2:]: {cities[-2:]}")
print()

print(f"cities[::]: {cities[::]}")
print()

state = "Missippippi"
print(f"state[:4]: {state[:4]}")

more_cities = ["Clifton", "Upper Marlboro", "Ballston", "Vienna"]
cities[2:4] = more_cities 
print(f"cities: {cities}")

cities[0:1] = ["Reston", "Herndon", "Chantilly"]
print(f"cities: {cities}")
print()

#  for VAR ... in ITERABLE:
#      ...

# for VAR in ITERABLE:
for city in cities:  # city = cities[0], city = cities[1], ...
    if city.startswith('C'):
        continue
    print(city)
    if city.startswith('U'):
        break
print('-' * 60)

a = "py"
b = "thon"
c = a + b
print(f"c: {c}")

r = [1, 2, 3, 4]
s = ['a', 'b', 'c']
t = r + s
print(f"t: {t}")

print(f"c * 5: {c * 5}")

print(f"s * 4: {s * 4}")

print('-' * 60)

flags = [True] * 25
print(f"flags: {flags}")
print()

for name in 'Clifton', 'Columbia', 'Chantilly', 'Tysons Corner', 'Baltimore':
    print(f"{name:15} {name in cities}")
print()

nums = [5, -3, 19, 4, 86, 4, 13, 4]

print(len(cities), len(nums))
print(min(cities), min(nums))
print(max(cities), max(nums))
print(sum(nums))
print(sorted(cities))  # not a generator
print(sorted(nums))

print(f"cities: {cities}")

rcities = reversed(cities)
print(f"rcities: {rcities}")
for city in rcities:
    print(city)
print("Again:")

capitals = ['Annapolis', 'Richmond', 'Raleigh']
states = ['Maryland', 'Virginia', 'North Carolina']

info = zip(capitals, states)
print(f"info: {info}")
print(f"list(info): {list(info)}")
info = zip(capitals, states)
for capital, state in info:
    print(f"{state:15} {capital}")
print()

for i, city in enumerate(cities):
    if (i % 3) == 0:
        print("*", end='')
    print(i, city)
print()
print('-' * 60)
for i, city in enumerate(cities, 1):
    print(f"{i:2d}. {city}")
print()

for i in range(5):
    print("Python is fun!")
print()

for i in range(1, 11):
    print(i, end=' ')
print('\n')

for i in range(5, 101, 5):
    print(i, end=',')
print('\n')
















