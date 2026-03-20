#!/usr/bin/python3


def max_two_sum(arr):
    if len(arr) < 2:
        return None
    sorted_arr = sorted(arr)
    return sorted_arr[-1] + sorted_arr[-2]

def max_pair_sum(arr):
    if len(arr) < 2:
        return None
    largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])


    for num in arr[2:]:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest:
            second_largest =num

    return largest + second_largest
