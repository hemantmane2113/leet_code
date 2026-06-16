from collections import Counter
from typing import List

class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        score = 0
        for key,value in counts.items():
            if value % k == 0:
                score = score + (key * value)
        return score
        #can also use list comprehension
        # return sum(key * value  for key,value in counts.items() if num % k == 0)