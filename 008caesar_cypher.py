# A simple Caesar cypher, shifting all the letters in a user's message by the amount specified by the user
# If the user has a key of 3 and a message of "Hello, world", the printed message will be "Khoor, zurog"

import sys

def cypher(key, message):
    result = ""
    # Shift chars in user input by key number, looping on an ASCII table
    for letter in message:
        if letter.isupper():
            shifted = (ord(letter) - ord('A') + key) % 26 # Turns capital letters into ascii
            result += chr(shifted + ord('A')) # Turns ascii back into capital letters, adds to result
        elif letter.islower():
            shifted = (ord(letter) - ord('a') + key) % 26 # Turns lower case letters into ascii
            result += chr(shifted + ord('a')) # Turns ascii back into lower case letters, adds to result
        else:
            result += letter
    # Print chars to user in shifted format, keeping punctuation and numbers
    print(result)


def main():
    while True:
        try:
            # Get user key input, numeric only
            key = int(input("Key: "))
            if key > 0:
                break
            else:
                print("Invalid input. The key must be greater than 0. Please try again.", flush=True)
        except ValueError:
            print("Invalid input. Please enter a numeric value greater than 0.", flush=True)
    message = input("Message: ") # Get user message input
    cypher(key, message)

if __name__ == "__main__":
    main()
