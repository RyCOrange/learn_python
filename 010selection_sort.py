# A simple selection sort algorithm that recursively revises the list of numbers provided
# The user would provide numbers with spaces in between them "3 2 4 1 5" and received a sorted list "1 2 3 4 5"

def selection_sort(split_list, n, index=0):
    # Base case: index reaches the end
    if index == n:
        return
        
    # Find minimum in the remaining unsorted array
    min_idx = index
    for j in range(index + 1, n):
        if split_list[j] < split_list[min_idx]:
            min_idx = j

    # Swap found minimum with the first element of unsorted part
    split_list[min_idx], split_list[index] = split_list[index], split_list[min_idx]

    # Recur for the rest of the array
    selection_sort(split_list, n, index + 1)

def main():
    user_series = input("What is your series of numbers? ") # Get user input of series of numbers
    split_list = [int(x) for x in user_series.split()]
    selection_sort(split_list, len(split_list))
    print(split_list) # Print revised list of numbers in order

if __name__ == "__main__":
    main()
