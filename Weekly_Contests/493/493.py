class Solution:
    def countCommas(self, n: int) -> int:
        score = 0 
        if n <= 100000:   
            for i in range(1,n+1):
                if i <= 999:
                    continue
                elif i >= 1000 and i <= 100000:
                    score = score + 1
        return score