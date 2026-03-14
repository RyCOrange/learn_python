# A basic bubble sort algorithm that "bubbles" the hgihest value number to the top of the list and works down from there
# Input of 2 3 5 4 1 will return [1, 2, 3, 4, 5]

def bubble_sort(split_list):
    n = len(split_list)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if split_list[j] > split_list[j + 1]: # Compares current value with next value
                split_list[j], split_list[j + 1] = split_list[j + 1], split_list[j] # Swaps value if current is larger than next
    
    return split_list

def main():
    user_list = input("Numbers: ") # Get user input
    split_list = [int(x) for x in user_list.split()]
    bubble_sort(split_list)
    print(split_list) # Print sorted list

if __name__ == "__main__":
    main()