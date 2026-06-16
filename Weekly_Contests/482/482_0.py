from typing import List
class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        opt_score = float('-inf')
        x = len(nums)
        prefixSum = 0
        for i in range(0,x-1):
            prefixSum = nums[i] + prefixSum
            suffixMin = min(nums[i+1:: ])
            if opt_score < prefixSum - suffixMin:
                opt_score = prefixSum - suffixMin
        return opt_score