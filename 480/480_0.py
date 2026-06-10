from typing import List
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        return (abs(sorted(nums[0:k])) - (sorted(nums[-k:-1])))#cannot substract list from list, we need to sum the elements of the lists before subtracting