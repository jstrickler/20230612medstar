
states = (
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
)

with open("states.txt", "w") as states_out: # "w" opens for writing, "a" for append
    for state in states:
        states_out.write(state + "\n")  # write() does not automatically add newline

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

with open('cpeople.txt', 'w') as cp_out:
    for person in people:
        # person is a tuple
        file_line = '|'.join(person) + '\n'
        cp_out.write(file_line)

with open('cpeople.txt') as cp_in:  # open for reading
    with open('cpeople_names.txt', 'w') as cp_out:   # open for writing
        for raw_line in cp_in:
            line = raw_line.rstrip()
            first_name, last_name, product, dob = line.split('|')
            line_to_write = f"{first_name} {last_name}\n"
            cp_out.write(line_to_write)