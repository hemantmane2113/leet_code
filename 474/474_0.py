from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        lower_bound = nums[0]
        upper_bound = nums[-1]
        missing_nums = []

        for i in range(lower_bound,upper_bound +1):
            if i not in nums:
                missing_nums.append(i)
        return missing_nums