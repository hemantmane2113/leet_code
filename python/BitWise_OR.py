from typing import List

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        even_list = []
        for num in nums:
            if num % 2 == 0:
                even_list.append(num)
                
        result = 0
        if even_list:
            for i in range(len(even_list)):
                result = even_list[i] | result
        else:
            return -1
            
        return result


def main():
    num_list = list(map(int, input().split()))
    obj1 = Solution()

    iRet = obj1.evenNumberBitwiseORs(num_list)

    if iRet == -1:
        print(0)   # this prints 0 for odd-only list
    else:
        print(iRet)


if __name__ == "__main__":
    main()
