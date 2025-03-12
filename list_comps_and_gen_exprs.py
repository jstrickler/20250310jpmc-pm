fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

# str bytes list tuple

f0 = []
for f in fruits:
    value = f.title()
    f0.append(value)
print(f"{f0 = }\n")

#       value             iterable
f1 = [f.title() for f in fruits]
print(f"{f1 = }\n")

#  new_list = [EXPR for VAR in ITERABLE if CONDITION]
f2 = [f.title() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f for f in fruits if len(f) > 8]
print(f"{f3 = }\n")

f4 = [fruit[:3] for fruit in fruits if len(fruit) > 8]
print(f"{f4 = }\n")

client_data = [('Bob', 123), ('Fred', 930), ('Mary', 393)]

#      (one element) (one-element) (iterables)
#      item-added     loop-var   list-items
nums = [client[1] for client in client_data]
print(f"{nums = }\n")

def double(x):
    return x * 2

f5 = [double(f) for f in fruits]
print(f"{f5 = }\n")

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

dobs = [p[3] for p in people]
print(f"{dobs = }\n")

fruit_list = [f.upper() for f in fruits]
fruit_iter = (f.upper() for f in fruits)
fruit_item_iterm = (f for f in fruits if f.startswith('a'))  # redundant
print(f"{fruit_iter = }")
for fruit in fruit_iter:
    print(fruit)
