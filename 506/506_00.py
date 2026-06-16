class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        square_sum = 0
        while n > 0:
            digit = n % 10   
           
            digit_sum = digit_sum + digit
            square_sum = square_sum + (digit * digit)

            n = n // 10
            
        if square_sum - digit_sum >= 50:
            return True
 
        return False