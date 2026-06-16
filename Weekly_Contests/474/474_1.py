from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
            
        # Convert to set for O(1) lookups
        num_set = set(nums) 
        
        # Find bounds in O(N) time instead of sorting
        lower_bound = min(nums)
        upper_bound = max(nums)
        
        # Linear scan for missing elements
        return [i for i in range(lower_bound, upper_bound + 1) if i not in num_set]