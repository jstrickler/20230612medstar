counts = {}  # create new empty dict

with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip()
        if breakfast_item in counts:   # check to see if current item in dict
            counts[breakfast_item] = counts[breakfast_item] + 1   # if so, increment count for specified key
        else:
            counts[breakfast_item] = 1 # else add new element 
        # counts[breakfast_item] = counts.get(breakfast_item, 0) + 1

for item, count in counts.items():
    print(item, count)

with open('../DATA/breakfast.txt') as br_in:
    all_foods = br_in.read().splitlines()
    print(f"all_foods: {all_foods}")
    unique_foods = set(all_foods)
    print(f"unique_foods: {unique_foods}")

    