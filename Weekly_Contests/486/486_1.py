from typing import List


def minimumPrefixLength(nums: List[int]) -> int:
    score = 0
    if nums == sorted(nums):
        score = 0
        return score
    
    

    for i in range(len(nums)-1,0,-1):
        if nums[i] > nums[i-1]: 
            continue
        else:
            score = i
            break

    return score

# example
nums = [-4,-10]
#nums = [4,3,-2,-5]

iret = minimumPrefixLength(nums)
print(iret)