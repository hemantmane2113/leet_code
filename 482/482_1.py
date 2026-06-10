from typing import List
class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        x = len(nums)
        
        # 1. Pre-calculate the suffix minimums from right to left
        suffixMin = [0] * x
        suffixMin[-1] = nums[-1]
        for i in range(x - 2, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])
            
        opt_score = float('-inf')
        prefixSum = 0
        
        # 2. Main loop matches your original design, but runs instantly
        for i in range(0, x - 1):
            prefixSum = nums[i] + prefixSum
            
            # Instant O(1) lookup instead of the slow min() slice
            current_min = suffixMin[i + 1]
            
            if opt_score < prefixSum - current_min:
                opt_score = prefixSum - current_min
                
        return opt_score