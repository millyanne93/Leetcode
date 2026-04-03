## Given a string, determine if it's a palindrome considering only:

Alphanumeric characters (letters A-Z, a-z, and numbers 0-9)

Ignore case (treat 'A' same as 'a')

Ignore non-alphanumeric characters (spaces, punctuation, etc.)

A palindrome reads the same forward and backward.

🎯 Examples

# Example 1:
Input: "A man, a plan, a canal: Panama"
Output: True
Explanation: After filtering: "amanaplanacanalpanama" (reads same forward/backward)

# Example 2:
Input: "race a car"
Output: False
Explanation: After filtering: "raceacar" (reverse is "racaeçar" - not the same)

# Example 3:
Input: " "
Output: True
Explanation: Empty string is considered valid palindrome

# Example 4:
Input: "0P"
Output: False
Explanation: After filtering: "0P" (reverse is "P0" - not same)

# Example 5:
Input: "Madam, I'm Adam"
Output: True
Explanation: "madamimadam" is a palindrome
