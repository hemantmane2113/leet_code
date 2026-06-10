from typing import List
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s_nums = sorted(nums)# first sort the list
        
        # Sum of the first k elements after sorting them
        first_k = sum(s_nums[:k])
        
        
        # Sum of the last k elements after sorting them
        last_k = sum(s_nums[-k:])
        
        return abs(first_k - last_k)