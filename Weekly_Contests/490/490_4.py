from typing import List

class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        p1 = True
        p2 = False
        p1_score = 0
        p2_score = 0
        
        for i in range(0, len(nums)):
            # RULE 1: If nums[i] is odd, swap roles
            if nums[i] % 2 != 0:
                if p1 == True and p2 == False:
                    p1 = False
                    p2 = True 
                elif p1 == False and p2 == True:
                    p1 = True
                    p2 = False
            
            # RULE 2: Changed 'elif' to 'if'. In every 6th game, swap roles again
            if i in [idx for idx in range(5, len(nums), 6)]:
                if p1 == True and p2 == False:
                    p1 = False
                    p2 = True 
                elif p1 == False and p2 == True:
                    p1 = True
                    p2 = False

            # RULE 3: Add points to whoever is active AT THE END of the sequential rules
            if p1 == True:
                p1_score += nums[i]
            elif p2 == True:
                p2_score += nums[i]
                
        return p1_score - p2_score
