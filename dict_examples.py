airports = {
   'EWR': 'Newark',
   'YYZ': 'Toronto',
   'SJU': 'San Juan',
   'MCI': 'Kansas City',
   'SFO': 'San Francisco',
   'RDU': 'Raleigh-Durham',
   'LTN': 'London',  # (Luton)
   'LGW': 'London',  # (Gatwick)
   'LHR': 'London',  # (Heathrow)
   'SJC': 'San Jose',
   'MCO': 'Orlando',
   'YCC': 'Calgary',
   'ABQ': 'Albuquerque',
   'OAK': 'Oakland',
   'SMF': 'Sacramento',
   'YOW': 'Ottawa',
   'IAD': 'Dulles',
}

for code, city in airports.items():
    print(code, city)
print()

print(f"{airports['MCO'] = }")
print(f"{airports.get('MCO') = }")
airports['MCO'] = 'Disney-World'
airports['WAW'] = 'Warsaw'
airports['GLA'] = 'Glasgow'
print(f"{airports = }")
print(f"{airports.get('ABC') = }")
print(f"{airports.get('ABC', 'NOPE!') = }")


