# A simple message encryption that takes a 26-char user key and shifts actual alphabet in the user input message to that new key
# Try with this key: NQXPOMAFTRHLZGECYJIUWSKDVB
# Writing "Hello" with this key should return "Folle"


# Encrypts the user's message with the key as an alphabet translation
def substitution(key, message):
    key = key.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = []

    # Subsititute ordered alphabet with user input string
    for char in message:
        if char.lower() in alphabet: 
            index = alphabet.index(char.lower()) # Translates letters in message
            encrypted_char = key[index]
            if char.isupper(): # Returns capital letters to a capital state to preserve casing
                encrypted_char = encrypted_char.upper()
            encrypted.append(encrypted_char)
        else:
            encrypted.append(char)  # Non-alpha chars unchanged

    return "".join(encrypted)

def main():
    # Requires user key string to be exactly 26 characters long
    while True:
        try:
            key = input("Key: ") # Get user key string
            if len(key) != 26:
                print("Key must be exactly 26 letters long") # Rejects shorter or longer than 26 char keys
            elif len(set(key.lower())) != 26:
                print("Key must have 1 of each letter") # Rejects keys with duplicate letters
            else:
                break
        except ValueError:
            print("Invalid key.")
        
    message = input("Message: ") # Get user message

    print(f"Encrypted: {substitution(key, message)}") # Print user message with substituted key

if __name__ == "__main__":
    main()