import sys
import os
#        0       1          2      3    4    ....
#   pygrep.py SEARCH-TERM FILE1 FILE2 FILE3 ...

search_term = sys.argv.pop(1)

for file_path in sys.argv[1:]:
    with open(file_path) as file_in:
        file_name = os.path.basename(file_path)
        for raw_line in file_in:
            if search_term in raw_line:
                print(file_name, raw_line.rstrip())
        