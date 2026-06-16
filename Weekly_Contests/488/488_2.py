from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        score = 0
        for i in range (0,len(nums)-1):
            for j in range(1,len(nums)):
                if nums[i] > sum(nums[i+1:len(nums)])/len(nums[i+1:len(nums)]):
                    score = score + 1
                    continue
        return score