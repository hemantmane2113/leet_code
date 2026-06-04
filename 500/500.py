class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:

        score_list = []
        for i in range(0,len(nums)):
            temp_list = []
            score = 0
            for j in range(i+1,len(nums)):
                temp_list.append(nums[j])
            if nums[i] % 2 == 0:
                for k in range(0,len(temp_list)):
                    if temp_list[k] % 2 != 0:
                        score = score + 1 
                score_list.append(score)
            else:
                for k in range(0,len(temp_list)):
                    if temp_list[k] % 2 == 0:
                        score = score + 1
                score_list.append(score)
            #score_list.append(score) --> just single append at the end(more efficient) 
        return score_list