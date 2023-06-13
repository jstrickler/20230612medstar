s1 = "sp\tam \n"    #  \n  \r \t \b \f \uxxx
print(len(s1))
s2 = 'spam\n'  # same as s1
s3 = """spam\n"""
s4 = '''spam\n'''

print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
print("""Guido's the ex-"BDFL" of Python""")

query = """select *
from customers
where state = 'NC'
order by balance
"""

