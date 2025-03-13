# define function
def say_hello():
    print("Hello, world")

say_hello()  # Call function

def process_files(search_term, *file_paths, ignore_case, **kwargs):
    for file_path in file_paths:
        print(file_path)

# e = Element('book', isbn="12345")
