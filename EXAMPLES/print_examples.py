city = 'Orlando' 
temperature = 85
hit_count = 5
average = 3.4563892382

print(city, temperature, hit_count, average)
# sep = " "
# end = "\n"
# output str(city) + sep + str(temperatrue) + sep + str(hit_count) + sep + str(average) + end
print()

print(city, end='=>')  # Print space instead of newline at the end
print(temperature)
print()

# Item separator is comma + space
print(city, temperature, hit_count, average, sep=", ")
print()

# Item separator is empty string
print(city, temperature, hit_count, average, sep="")
print()

print(city + ": " + str(temperature))
print(city, temperature, sep=": ")
print(f"{city}: {temperature}")

#  f"{var} {var} {var} other stuff {var}"
print(f"2 + 2 is {2 + 2}")
