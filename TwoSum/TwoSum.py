class Solution(object):
    def twoSum(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Approach: Hash Map (One-pass)
        - Store each number's index as we iterate
        - For current number, check if complement exists in map
        - If yes, we found our pair
        
        Time complexity: O(n) - single pass through array
        Space complexity: O(n) - worst case store n-1 elements
        
        Why this approach?
        - Brute force would be O(n²) - too slow
        - Sorting + two pointers would be O(n log n) - good but not optimal
        - Hash map gives us O(1) lookup, making it O(n) total
        """
        # Dictionary to store numbers and their indices
        lookup = {}
        
        # Loop through the list
        for index, num in enumerate(arr):
            # Calculate the complement of the current number
            complement = target - num
            
            # Check if complement is already in the dictionary
            if complement in lookup:
                # If found, return the indices of the complement and the current number
                return [lookup[complement], index]
            
            # store the current number and its index in the dictionary
            lookup[num] = index
        
