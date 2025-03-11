cities = []  # empty list

cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"{cities[0] = }")
print(f"{len(cities) = }")

print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
cities.insert(-3, "Birmingham")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
print(f"cities: {cities}\n")

# LIST.append(obj) LIST.insert(idx, obj) LIST.extend(iterable)

del cities[3]   # del x    del  x[idx]
print(f"cities: {cities}\n")

VALUE = "Buffalo"
if VALUE in cities:
    POS = cities.index(VALUE)
    cities.remove(VALUE)
print(f"cities: {cities}\n")

city = cities.pop()   # remoes LAST value
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

cities[2] = "Sacramento"
print(f"{cities = }")

# cities[25] = "Philadelphia"  ERROR ERROR ERROR WARNING WILL ROBINSON

# del LIST[idx]  LIST.remove(value) LIST.pop() LIST.pop(idx)