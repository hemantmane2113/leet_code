from typing import List
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
          n = len(nums)

          for i in range(n):
               for j in range(0, n-i-1):
                    if nums[j] > nums[j+1]:
                         nums[j], nums[j+1] = nums[j+1], nums[j]
          first_k = sum(nums[:k])
          last_k = sum(nums[-k:])
          return abs(first_k - last_k)