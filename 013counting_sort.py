# Sorts a user input array separated by spaces by the count of each value



def counting_sort(split_list):
    max_val = max(split_list) # Finds highest value in the array
    count = [0] * (max_val + 1) # Creates a new array that is 1 object longer than the counted array

    for num in split_list:
        count[num] += 1 # Count occurrences of each value in array

    i = 0
    for val in range(max_val + 1): # Iterates over whole array
        while count[val] > 0: # Rearrange array by order of lowest value
            split_list[i] = val # Adds the value that is currently being iterated over
            i += 1
            count[val] -= 1
    return split_list

def main():
    user_input = input("Array: ") # Get user input
    split_list = [int(x) for x in user_input.split()] # Splits string into array
    counting_sort(split_list)
    print(split_list) # Prints sorted list

if __name__ == "__main__":
    main()