
m = "Missippippi"
x = "sip"

print(x in m)

a = "Py"
b = "thon"
c = a + b
print(c)

print(len(c))      # len() is function
print(c.upper())   # .upper() is method

actor = "Chris Hemsworth"

a = actor.upper()
print(a)
print(actor.upper())

print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))  # method chaining    a.b().c().d()

#  CALLABLE()   function(args?)    obj.method(args?)    Class(args?)  
#   VARIABLE     variable       obj.attribute 

print(actor)
print(actor.find('wo'))
print(actor.find('Chris'))
print(actor.find('Liam'))
print()

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
#  also .endswith(...)

file_name = 'wombats.txt'
print(file_name.removesuffix('.txt'))

s = "       All my exes live in Texas        "
print(s + "|")
print(s.lstrip() + "|")
print(s.rstrip() + "|")
print(s.strip() + "|")

raw_amount = "$$$2345"
amount = raw_amount.lstrip('$')
print(raw_amount, amount)

print(actor.replace('Chris', 'Liam'))

print(actor.replace('h', 'Z'))
print(actor.replace('h', 'Z', 1))


note_string = "do     re mi fa    so la    ti       do"
notes = note_string.split()  # split on whitespace   \n \r sp \t \f \b
print(notes)

data = "spam:ham:toast:eggs"
fields = data.split(':')  # split on a string
print(fields)

print("|".join(fields))
print("/".join(fields))
print("\t".join(fields))



contents = "Mary had a little lamb\nThe lamb was white as snow\nIt followed her to school"
print(contents)

lines = contents.splitlines()
print(lines)






















