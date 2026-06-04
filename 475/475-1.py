# lot of mistakes
# big O is O(n^3)

from typing import List

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        tup = ()
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                for k in range(0,len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        tup.add(i)
                        tup.add(j)
                        tup.add(k)
        print(tup)
        value = 0
        for num in range(0,len(nums)):
            for v in range(0,len(tup)):
                value = abs(tup[0]-nums[tup[0]+1]) + abs(tup[1]-nums[tup[1]+1]) + abs(tup[0]-nums[tup[0]+1])
                return value 

def main():
    num = int(input())

    iobj = Solution()

    iRet = iobj.minimumDistance(num)
    print(iRet)

if __name__ == "__main__":
    main()