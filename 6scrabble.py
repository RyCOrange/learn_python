# A short 2-player game based on scrabble
# 2 players put in their words, the player with the highest-point word wins

# Get player 1 input
# Get player 2 input
# Pull each letter points from points array
# Sum each player points
# Check player points against each other, check for win or tie
# Print winner

def points_calc1(word1):
    points = 0
    lets = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    for letter in word1:
        if letter.isupper():
            points = lets[ord(letter) - ord('A')] + points
        elif letter.islower():
            points = lets[ord(letter) - ord('a')] + points
    return(points)

def points_calc2(word2):
    points = 0
    lets = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
    for letter in word2:
        if letter.isupper():
            points = lets[ord(letter) - ord('A')] + points
        elif letter.islower():
            points = lets[ord(letter) - ord('a')] + points
    return(points)

def main():
    word1 = input("Player 1 word: ")
    word2 = input("Player 2 word: ")
    if points_calc1(word1) > points_calc2(word2):
        print(f"Player 1 wins with {word1}!")
    elif points_calc1(word1) < points_calc2(word2):
        print(f"Player 2 wins with {word2}!")
    else:
        print("Tie!")

if __name__ == "__main__":
    main()