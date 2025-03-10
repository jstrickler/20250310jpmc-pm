import sys
import os.path

for path_name in sys.argv[1:]:
    if os.path.isdir(path_name):
        print(f"ERROR! {path_name} is a directory")
        continue
    else:
        print(path_name, os.path.getsize(path_name))
