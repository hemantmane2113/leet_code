class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        final = 0
        sorted_nums = sorted(nums,reverse = True)
        
        for i in range(k):
            for _ in sorted_nums:
                if mul != 0:
                    final = final + sorted_nums[i]  * mul
                    mul = mul - 1
                   
                else: 
                    final = final + sorted_nums[i]
                break
                        
        return final
        