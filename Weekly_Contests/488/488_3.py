from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        score = 0
        for i in range (0,len(nums)-1):
            
            j = len(nums) # FIXED: Set j to look at the entire right side of the array at once
            
            if nums[i] > sum(nums[i+1:j])/len(nums[i+1:j]):# FIXED: Used true division '/' instead of '//' to handle decimals (e.g., 3.5)
                score = score + 1
                continue
        return score