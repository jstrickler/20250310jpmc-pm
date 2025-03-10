DIRTY_STRINGS = [
    "  mud   ",
    "grime  ",
    "   filth    ",
    "     messy messy     ",
    "DIRT	",
    "       FILTH and grime    ",
    "Dirt",
    "   Filth, dirt, grime, grime, grime, filth, and mud      ",
]

def main():
    for old_string in DIRTY_STRINGS:
        new_string = cleanup(old_string)
        print(f"Before: >{old_string}<\nAfter:  >{new_string}<\n")

# define a function cleanup() here
# cleanup() should take one argument -- the string to be 
# cleaned up -- and should return a cleaned up copy

main()
