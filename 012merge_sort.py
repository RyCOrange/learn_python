# A simple merge sort algorithm. This takes an array of numbers separated by spaces and recursively separates into 2 groups to compare
# Merges 2 groups in order of smallest to largest until array is sorted

def merge_sort(split_list):
    if len(split_list) <= 1:
        return split_list
    
    mid = len(split_list) // 2 # Slice array in half
    left = split_list[:mid] # Separates left half of array
    right = split_list[mid:] # Separates right half of array

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    while left and right: # Loops through process while both arrays have values
        if left[0] < right[0]: # Compare left and right half
            result.append(left.pop(0)) # Merge left if less than right
        else:
            result.append(right.pop(0)) # Merge right if less than left
    
    result.extend(left) # Adds left value to array if 1 value is left
    result.extend(right) # Adds right value to array if 1 value is left

    return result

def main():
    user_input = input("Array: ") # Get user input
    split_list = [int(x) for x in user_input.split()] # Splits string into array
    print(merge_sort(split_list)) # Print sorted list

if __name__ == "__main__":
    main()