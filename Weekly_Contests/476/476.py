
from typing import List
class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        max1 = nums[-1]
        max2 = nums[-2]
        min = nums[0]

        output = max1 + max2 - min

        return output
    
def main():
    num = int(input())

    iobj = Solution()

    iRet = iobj.maximizeExpressionOfThree(num)
    print(iRet)

if __name__ == "__main__":
    main()