from typing import List

class Solution:
     
    def scoreDifference(self, nums: List[int]) -> int:
        p1 = True
        p2 = False
        p1_score = 0
        p2_score = 0
        
        for i in range(0,len(nums)):
            if nums[i] % 2 != 0:
                if p1 == True and p2 == False:
                    p1 = False
                    p2 = True 
                elif p1 == False and p2 == True:
                    p1 = True
                    p2 = False
                    
            elif nums[i] % 2 == 0:
                if p1 == True and p2 == False:
                    p1 = True
                    p2 = False
                elif p1 == False and p2 == True:
                    p1 = False
                    p2 = True
                    
            if i in [ i for i in range(5,len(nums),6)]:
                if p1 == True and p2 == False:
                    p1 = False
                    p2 = True 
                elif p1 == False and p2 == True:
                    p1 = True
                    p2 = False

            if p1 == True:
                p1_score += nums[i]
            elif p2 == True:
                p2_score += nums[i]
            
        return p1_score - p2_score
                
        