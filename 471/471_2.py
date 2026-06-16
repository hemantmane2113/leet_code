from typing import List
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        # Directly sum the numbers that are divisible by k
        return sum(num for num in nums if num % k == 0)