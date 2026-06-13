from typing import List
class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        total = 0
        sign = 1
        for num in nums:
            total += num * sign
            sign = -sign
        return total
