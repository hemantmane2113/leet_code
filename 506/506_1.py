class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digits_list = [int(d) for d in str(n)]
        
        digit_sum = sum(digits_list)
        square_sum = sum(d * d for d in digits_list)
        
        return (square_sum - digit_sum) >= 50