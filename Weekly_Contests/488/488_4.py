from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        score = 0
        right_sum = 0
        right_count = 0
        
        # Iterate from the rightmost element to the first element
        for i in range(len(nums) - 1, -1, -1):
            if right_count > 0:
                # Calculate the exact average of all elements to the right
                avg = right_sum / right_count
                if nums[i] > avg:
                    score += 1
            
            # Update the running sum and count for the next element to the left
            right_sum += nums[i]
            right_count += 1
            
        return score