# Big O --> O(n)

from typing import List
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums_sorted = sorted(nums)

        # If k == 0 → all elements qualify
        if k == 0:
            return n

        # If no element has k greater ones
        if k >= n:
            return 0

        threshold = nums_sorted[n - k - 1]

        for x in nums:
            if x<= threshold:
                sum = sum + 1
        
        return sum

        #return sum(1 for x in nums if x <= threshold)
    
def main():
    nums = list(map(int, input().split()))
    k = int(input())

    obj = Solution()
    iRet = obj.countElements(nums, k)
    print(iRet)

# Example usage
if __name__ == "__main__":
    main()