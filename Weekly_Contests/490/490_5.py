from typing import List

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        score_diff = 0
        current_player = 1  # 1 represents Player 1, -1 represents Player 2
        
        for i, val in enumerate(nums):
            # Rule 1: Swap if value is odd
            if val % 2 != 0:
                current_player = -current_player
                
            # Rule 2: Swap if it is every 6th game (index 5, 11, 17...)
            if i % 6 == 5:
                current_player = -current_player
                
            # Rule 3: Add/subtract score in a single line
            score_diff += val * current_player
            
        return score_diff
