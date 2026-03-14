# A voting scheme where the candidates are assigned to their class, then the number of votes are decided, then the votes are cast
# The winner is determined by a simple sorting algorithm that compares the candidates in the list

# Define candidate class
class candidate:
    def __init__(self, name, votes):
        self.name = name
        self.votes = votes

def votes(candidate_list, num_voters):
    for i in range(num_voters): # Get user input of votes iterated over number of voters
        vote = input("Votes: ")
        for j in candidate_list: # Iterates through every candidate in the list
            if j.name == vote: # Checks if vote name is in the list
                j.votes += 1 # Assign individual votes to candidates

def print_winner(candidate_list):
    winner = candidate_list[0] # Sets candidate[0] as the default winner

    for i in candidate_list: # Find max number of votes
        if i.votes > winner.votes: # compares current winner with the current iteration of votes in the list
            winner = i # If current iteration has more votes than current winner, the current iteration becomes current winner
    
    # Print candidate(s) with max votes
    print(f"Winner is {winner.name} with {winner.votes} votes")

def main():
    candidates = input("Candidates: ") # Get user input of candidates
    split_list = candidates.split() # Splits string into array
    num_voters = int(input("Number of voters: ")) # Get user input of number of voters

    candidate_list = [candidate(name, 0) for name in split_list]

    votes(candidate_list, num_voters) # Assigns votes to candidates
    print_winner(candidate_list) # Determine winner(s) of election


if __name__ == "__main__":
    main()