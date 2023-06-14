
set0 = set()
set1 = {'red', 'blue', 'green', 'purple', 'green'}  # create literal set
set2 = {'green', 'blue', 'yellow', 'orange', 'blue', 'blue', 'green'}
#  set3 = set(any-iterable-of-immutable-values)

set1.add('taupe')  # add element to set (ignored if already in set)
set2.add('purple')
set2.add('purple')
set1.add('chartreuse')

print(set1)
print(set2)
print(set1 & set2)  # intersection of two sets -- common items
print(set1 ^ set2)  # XOR (symmetric difference) -- items in one set but not both
print(set1 | set2)  # union of two sets -- distinct combination of both sets
print(set1 - set2)  # difference -- Remove items in right set from left set
print(set2 - set1)  # difference
print()

with open('../DATA/breakfast.txt') as breakfast_in:
    food = breakfast_in.read().splitlines()

unique_food = set(food)  # Create set from iterable (e.g., list)
print(unique_food)
