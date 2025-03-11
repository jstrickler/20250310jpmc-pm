values = ['a', 'b', 'c']

x, y, z = values  # unpack values (which is an iterable) into individual variables

print(x, y, z)
print()

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple', 'NeXT'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey', 'Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux', 'git'),
    ('John', 'Strickler'),
]

for row in people:
    first_name, last_name, *_ = row  # unpack row into variables
    print(first_name, last_name)
print()

for first_name, last_name, *products in people:  # a for loop unpacks if there is more than one variable
    print(first_name, last_name)
    for product in products:
        print(f"    {product}")
print()


fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

del fruits[1:4]
print(f"{fruits = }")
