d1 = dict()   # empty dict
d2 = {'a': 5, 'm': 99, 'x': 4, 'c': 5}
d3 = {}   # empty dict
print(f"d2: {d2}")

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'LTN': 'London',  # (Luton)
    'LGW': 'London',  # (Gatwick)
    'LHR': 'London',  # (Heathrow)
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

airports['BWI'] = "Baltimore"
airports['PTI'] = "Piedmont Triad"  # Greensboro, NC
print(f"airports: {airports}")
airports['BWI'] = "Linthicum"
print(f"airports: {airports}")

print(f"airports['LHR']: {airports['LHR']}")
# print(f"airports['ROM']: {airports['ROM']}")
print(f"airports.get('ROM'): {airports.get('ROM')}")
print(f"airports.get('ROM', 'not found'): {airports.get('ROM', 'not found')}")

print(f"airports.setdefault('ROM', 'Rome'): {airports.setdefault('ROM', 'Rome')}")
print(f"airports: {airports}")
print()
#  for k, v in DICT.items():
#      ...

for code, city in sorted(airports.items()):
    print(code, city)
print()










