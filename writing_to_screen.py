person = "Fred Flintstone"
city = "Bedrock"
amount = 932.39029395

print(person, city, amount)
print("fun with print()")

# print() adds spaces between objects, and \n after them all

#   str(person) + ' ' + str(city) + ' ' + str(amount) + '\n'
#   str(person) + sep + str(city) + sep + str(amount) + end

print(person, city, amount, sep="/")
print(person, city, amount, sep=", ")

print("Py", end="")
print("thon")

print("foo", end=" ")
print("bar")

#  Bedrock, Fred Flintstone
print(f"city: {city}")
print(city, ",", person)
print(city + ", " + person)  # not so good....
print(f"{city}, {person}")   # f-string (AKA format string)
print(f"2 + 2 = {2 + 2}")

x = 5
print(f"x: {x}")
print(f"city: {city}")

print(f"amount: {amount:.1f}")

print(f"x: {x:4d}")
print(f"x: {x:04d}")

print("{}, {}".format(city, person))   
print("amount: {:.1f}".format(amount))




