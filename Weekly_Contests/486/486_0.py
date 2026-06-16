
from typing import List


def minimumPrefixLength(nums: List[int]) -> int:
    
    if nums == sorted(nums):
        score = 0
        return score
    
    

    for i in range(len(nums)-1,0,-1):
        if nums[i] > 0 and nums[i] > nums[i-1]:
            score = len(nums[:i-1]) 
            continue
        elif nums[i] < 0 and nums[i] < nums[i-1] :
            for index, value in enumerate(nums):
                nums[index] = abs(value)
            score = len(nums[i-1::-1]) 
            continue
        else:
            break

    return score

# example
#nums = [-4,-10]
nums = [4,3,-2,-5]

iret = minimumPrefixLength(nums)
print(iret)

        