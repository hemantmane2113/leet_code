# Big O -> O(n^2)

from typing import List

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # quick edge-cases
        if k == 0:
            return n
        if k >= n:
            return 0

        final_counter = 0
        for i in range(n):
            counter = 0
            for j in range(n):
                # count elements strictly greater than nums[i]
                if nums[j] > nums[i]:
                    counter += 1
            if counter >= k:
                final_counter += 1

        return final_counter


def main():
    nums = list(map(int, input().split()))
    k = int(input())

    obj = Solution()
    iRet = obj.countElements(nums, k)
    print(iRet)

# Example usage
if __name__ == "__main__":
    main()

