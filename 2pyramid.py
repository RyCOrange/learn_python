# Create a pyramid of pound symbols with a user input height


while True:
    try:
        # Get user input
        height = int(input("Enter a height between 1 and 8: "))
        # Check if user input is between 1 and 8
        assert 1 <= height <= 8
        break
    # Rejects numbers outside of range
    except (ValueError, AssertionError):
        print("Input must be between 1 and 8.")

stack = 0
line = 0

# Iterates multi line stack through user input
while stack < height:
    # Iterates single line print through user input
    while line < height - 1:
        print(" ", end='')
        line += 1
    print("#", end='')
    # Fills out the middle of the pyramid
    for i in range(stack * 2):
        print("#", end='')
    print("#")
    stack += 1
    line = stack
