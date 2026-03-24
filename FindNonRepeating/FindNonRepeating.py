#!/usr/bin/python3

def first_unique_char(s):
    """Find the first non-repeating character in a string 
    Example : leetcode - 'l'
    Example : loveleetcode - 'v'
    Example : aabb - None
    """
    # Create an empty dictionary to store character frequencies
    # This will hold each character and how many time it appears
    # Example : {'a':2, 'b':3, 'c':1}
    counts = {}

    #Loop through each character in the string in order
    for char in s:
        # For the current character, get its current count from the dictionary
        # .get(char, 0) means:
        # - if char exists in dictionary, return its value(current count)
        # - if char does NOT exist, return 0 (meaning seen 0 times so far)
        # Then add 1 to that value (because we are seeing it now)
        # Finally store the new count back in the dictionary
        counts[char] = counts.get(char, 0) +1

    # After this loop, counts dictionary contains:
    # Example: "Leetcode" - {'L':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}
    # Each key is a character, each value is how many times it appears

    #Loop through each character in the string again (preserving original order)
    for char in s:
        # Look up thi character's count in the dictionary
        # This is 0(1) Lookup - instantly get the count scanning string
        # Check if the count equals 1: (meaning it appears exactly once
        if counts[char] == 1:
            # Found it! Return this character immediately
            # This is the FIRST character that appears only once
            return char

    # If we complete the entire Loop without finding any character with count 1,
    # that means every character repeats at least once
    # Return None to indicate no unique character exists
    return None


