
from typing import List


def minimumPrefixLength(nums: List[int]) -> int:
    score = 0  # Initialize score at the top
    
    # Check if already strictly increasing (handles duplicates correctly)
    if all(nums[i] < nums[i+1] for i in range(len(nums)-1)):
        return 0

    # Scan backwards from right to left
    for i in range(len(nums)-1, 0, -1):
        # As long as the right element is strictly greater than the left element
        if nums[i] > nums[i-1]:
            continue
        else:
            # The moment the rule breaks, everything to the left (including index i-1) must go
            score = i
            break

    return score


# example
nums = [-4,-10]
#nums = [4,3,-2,-5]

iret = minimumPrefixLength(nums)
print(iret)
