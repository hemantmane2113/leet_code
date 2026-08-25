from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        i = 0  # pointer to current start of the array

        while i < len(nums):
            # Check if remaining array has duplicates
            remaining = nums[i:]
            if len(remaining) == len(set(remaining)):
                break

            operations += 1

            # Remove first three elements
            if i + 3 >= len(nums):
                break
            else:
                i += 3

        return operations
