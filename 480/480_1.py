from typing import List
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        # Sum of the first k elements after sorting them
        first_k = sum(sorted(nums[:k]))
        
        # Sum of the last k elements after sorting them
        last_k = sum(sorted(nums[-k:]))
        
        return abs(first_k - last_k)
    """
    The order of operations would be:
    1.slicing: nums[:k]
    2.sorting: sorted(nums[:k])
    3.summing: sum(sorted(nums[:k]))

    but we needed a whole sorted list to find the k largest and k smallest elements, 
    so we need to sort the entire list first and then slice it to get the required elements for summing.
    
    """