from typing import List

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        # Sorts based on: 1) the bit-reversed value, 2) the original value as a tie-breaker
        return sorted(nums, key=lambda x: (int(bin(x)[2:][::-1], 2), x))
