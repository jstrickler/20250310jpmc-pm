person = "Bill", "Gates", "Microsoft", "1955-10-28"
print(person, "\n")
print(f"{type(person) = }")

print(person[0], person[1], "\n")

first_name, last_name, product, dob = person  # unpack iterable to variables
given_name, family_name, product, dob = person  # unpack iterable to variables

person = "Steve", "Gates", "Microsoft", "1955-10-28"
print(f"{first_name = }")

first_name = "Robbie"
print(f"{person = }")


print(first_name, last_name, "\n")
print(f"{len(person) = }\n")
