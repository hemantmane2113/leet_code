# Big O -> O(nlog n)

from typing import List

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums)
        n = len(nums)

        answer = 0
        for x in nums:
            # number of elements strictly greater than x
            greater = n - self.upper_bound(nums_sorted, x)
            if greater >= k:
                answer += 1
        
        return answer

    def upper_bound(self, arr, x):
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo

def main():
    nums = list(map(int, input().split()))
    k = int(input())

    obj = Solution()
    iRet = obj.countElements(nums, k)
    print(iRet)

# Example usage
if __name__ == "__main__":
    main()