# Similar to 2pyramid, this creates a pyramid of # signs
# This time, there is a split in the pyramid

def make_pyramid(height):
    stack = 0
    line = 0
    # Iterates multi line stack through user input
    while stack < height:
        # Iterates single line print through user input
        while line < height - 1:
            print(" ", end='')
            line += 1
        print("#", end='')
        # Prints the left half of the pyramid
        for left in range(stack):
            print("#", end='')
        # Prints the center divide
        print("  ", end='')
        # Prints the right half of the pyramid
        for right in range(stack + 1):
            print("#", end='')
        print("\n", end='')
        stack += 1
        line = stack

def main():
    height = int(input("How tall: "))
    make_pyramid(height)

if __name__ == "__main__":
    main()