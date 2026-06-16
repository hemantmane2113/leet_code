from typing import List
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        full_range = set(range(min(nums), max(nums) + 1))
        return list(full_range - set(nums))