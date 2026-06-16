from typing import List
from functools import reduce
import operator

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        # Filter for even numbers first
        even_nums = [num for num in nums if num % 2 == 0]
        
        # If no even numbers exist, return 0. Otherwise, run bitwise OR across all.
        return reduce(operator.or_, even_nums, 0)