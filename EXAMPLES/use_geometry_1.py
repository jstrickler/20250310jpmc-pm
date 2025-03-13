import geometry  # find and load geometry.py
import sys
import re

circle = geometry.circle_area(8)
print(f"{circle = }")

rectangle = geometry.rectangle_area(10, 12)
print(f"{rectangle = }")

square = geometry.square_area(7.9)
print(f"{square = }")

# search locations
# 1. current folder
# 2. folders in PYTHONPATH  Windows: "F1;F2;F3"   Mac/Linux:  "F1:F2:F3"
# 3. <INSTALLATION-FOLDER>/lib
for path in sys.path:
    print(path)
print()
print(f"{sys.prefix = }")

print(f"{sys.modules['re'] = }")
print(f"{sys.modules['sys'] = }")
print(f"{sys.modules['geometry'] = }")
