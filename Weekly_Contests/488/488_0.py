from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        score = 0
        for i in range (0,len(nums)-1):
            for j in range(i,len(nums)):
                if nums[i] > sum(nums[i+1:j+1])//len(nums[i+1:j+1]):
                    score = score + 1
                    continue
        return score