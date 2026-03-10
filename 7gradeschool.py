# This project calculates the reading grade level based on the Coleman-Liau Index
# It separates levels by "Before Grade 1", grades 1 through 16, and "Grade 16+"

import string

# Calculate average number of letters per 100 words in text
def avg_letters(user_string):
    lets = 0
    spaces = user_string.count(" ") + 1
    cleaned_string = ''.join(e for e in user_string if e.isalnum())
    for letters in cleaned_string:
        lets += 1
    avg_lets = (lets / spaces) * 100
    return avg_lets

# Calculate average number of sentences per 100 words in text
def avg_sentences(user_string):
    puncts = 0
    for char in user_string:
        if char in ('.', '?', '!'):
            puncts += 1
    spaces = user_string.count(" ") + 1
    avg_sents = (puncts / spaces) * 100
    return avg_sents

def main():
    L = 0
    S = 0
    # Get user input string
    user_string = input("Text: ")
    L = avg_letters(user_string)
    S = avg_sentences(user_string)
    # Computer Coleman-Liau Index = 0.0588 * L - 0.296 * S - 15.8
    cole_liau = 0.0588 * L - 0.296 * S - 15.8
    if round(cole_liau) >= 1 and round(cole_liau) <= 16: # Print grade level
        print(f'Grade {round(cole_liau)}')
    elif round(cole_liau) < 1: # If grade level too low, print "Before Grade 1"
        print("Before Grade 1")
    else: # If grade level too high, print "Grade 16+"
        print("Grade 16+")

if __name__ == "__main__":
    main()
