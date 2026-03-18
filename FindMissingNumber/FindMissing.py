#!/usr/bin/python3

def find_missing(arr):
    """
    Find the smallest missing positive integer.

    This function takes an array of integers and returns the smallest
    positive integer (starting from 1) that is not present in the array.
    """
    seen = set(arr)
    n = 1
    while True:
        if n not in seen:
            return n
        n += 1
