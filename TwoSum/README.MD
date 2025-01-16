# Two Sum Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the `target`.

You may assume that each input will have **exactly one solution**, and you may not use the same element twice.

You can return the answer in **any order**.

---

## Examples
```plaintext
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] == 6, so we return [1, 2].

Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: nums[0] + nums[1] == 6, so we return [0, 1].

---

## Constraints
```plaintext
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

---
## Notes
```plaintext
Make sure not to use the same element twice.
Solutions can be returned in any order.
