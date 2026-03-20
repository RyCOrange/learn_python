# A voting scheme where the candidates are ranked on votes and 
# assigned to their class, then the number of votes are decided, then the votes are cast
# The winner is determined by a simple sorting algorithm that compares the candidates in the list

# Define candidate class
class candidate:
    def __init__(self, name, vote_rank):
        self.name = name
        self.vote_rank = vote_rank

def votes(candidate_list, num_voters):
    for i in range(num_voters):
        print(f"\nVoter {i + 1}:")
        for rank in range(1, 4):  # ranks 1, 2, 3
            name = input(f"Rank {rank}: ").strip()
            for candidate in candidate_list: # The lower the voter rank, the better the score
                if candidate.name == name:
                    candidate.vote_rank += rank
    
def print_winner(candidate_list):
    winner = candidate_list[0] # Sets candidate[0] as the default winner

    for i in candidate_list: # Find max number of votes
        if i.vote_rank > winner.vote_rank: # compares current winner with the current iteration of votes in the list
            winner = i # If current iteration has more votes than current winner, the current iteration becomes current winner
    
    # Print candidate(s) with max votes
    print(f"Winner is {winner.name}")

def main():
    candidates = input("Candidates: ") # Get user input of candidates
    split_list = candidates.split() # Splits string into array
    num_voters = int(input("Number of voters: ")) # Get user input of number of voters

    candidate_list = [candidate(name, 0, 0) for name in split_list]

    votes(candidate_list, num_voters) # Assigns votes to candidates
    print_winner(candidate_list) # Determine winner(s) of election


if __name__ == "__main__":
    main()