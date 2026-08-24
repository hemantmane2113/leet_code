from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0

        while nums and len(nums) != len(set(nums)):
            operations += 1

            if len(nums) <= 3:
                nums.clear()
            else:
                nums = nums[3:]

        return operations