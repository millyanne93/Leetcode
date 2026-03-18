#!/usr/bin/python3

#Returns First Duplicate Number
def first_duplicate(arr):
    seen = set() #Beginning with an empty set

    for num in arr:  # Loop through each number in the array
        if num in seen:  # Check if the number exists in seen 
            return num  #Return the first Duplicate
        seen.add(num)   # Havent seen the number yet, add it 

    return -1 # No duplicates 
