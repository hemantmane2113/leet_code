from typing import List
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l = len(nums)
        # Convert to a set for instant O(1) lookups
        num_set = set(nums)
        
        # Check each multiple from 1 to l + 1
        for i in range(1, l + 2):
            multiple = k * i
            if multiple not in num_set:
                return multiple