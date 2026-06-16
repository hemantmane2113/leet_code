from collections import Counter
from typing import List

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        
        # Check if the number (key) is divisible by k, then multiply by its frequency (value)
        return sum(key * value for key, value in counts.items() if key % k == 0)