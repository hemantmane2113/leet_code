from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        score = 0
        for i in range (0,len(nums)-1):
            # 1. FIXED: Start j at i + 1 to prevent empty slices and zero division
            for j in range(i+1,len(nums)):
                # 2. FIXED: Only perform the check on the very last iteration of j
                if j == len(nums) - 1:
                    # 3. FIXED: Changed // to / to accurately handle decimals (like 3.5)
                    if nums[i] > sum(nums[i+1:j+1])/len(nums[i+1:j+1]):
                        score = score + 1
                        continue
        return score