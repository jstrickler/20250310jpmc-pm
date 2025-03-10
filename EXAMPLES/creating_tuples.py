person = "Bill", "Gates", "Microsoft", "1955-10-28"
print(person, "\n")

print(person[0], person[1], "\n")

first_name, last_name, product, dob = person  # unpack iterable to variables
print(first_name, last_name, "\n")
print(f"{len(person) = }\n")
