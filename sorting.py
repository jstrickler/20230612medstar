fruits = ['pomegranate', 'cherry', 'apricot', 'Apple',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

f0 = sorted(fruits)
print(f"f0: {f0}\n")

#  str.lower(s)

f1 = sorted(fruits, key=str.lower)
print(f"f1: {f1}\n")

f2 = sorted(fruits, key=len)
print(f"f2: {f2}\n")

def ignore_case(original_value):
    comparison_value = original_value.lower()
    print(f"Comparing {original_value} as {comparison_value}")
    return comparison_value

f3 = sorted(fruits, key=ignore_case)
print(f"f3: {f3}\n")

def cust1(item):
    return len(item), item.lower()  # key function can return tuple of values

f4 = sorted(fruits, key=cust1)
print(f"f4: {f4}\n")

nums = [400, 23, 42, 800, 81, 9, 4, -32]
n1 = sorted(nums)
print(f"n1: {n1}\n")

n2 = sorted(nums, key=str)
print(f"n2: {n2}\n")

n3 = sorted(nums, key=abs)
print(f"n3: {n3}\n")

f5 = sorted(fruits, key=lambda f: (len(f), f.lower()))
print(f"f5: {f5}\n")

# lambda param: (value)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(person):
    return person[-1]

for person in sorted(people, key=by_dob):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: p[-1]):
    print(person)
print('-' * 60)

airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}
print(f"airports.items(): {airports.items()}\n")
print()

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

def by_value(element):
    return element[1], element[0]

for code, city in sorted(airports.items(), key=by_value):
    print(code, city)
print('-' * 60)

fruits.sort(key=str.lower)
print(f"fruits: {fruits}\n")

fruits.sort(key=str.lower, reverse=True)
print(f"fruits: {fruits}\n")

for code, city in sorted(airports.items(), key=by_value, reverse=True):
    print(code, city)
print('-' * 60)










