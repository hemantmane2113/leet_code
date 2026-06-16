from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        l = len(nums)
        multiples = [k * i for i in range(1,l+1)]
        for i in multiples:
            if i not in nums:
                return i

        return k * (l + 1)# If all generated multiples exist, the missing one is the next multiple