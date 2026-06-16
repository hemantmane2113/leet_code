class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        reversed_num = 0
        
        while n > 0:
            digit = n % 10
            reversed_num = (reversed_num * 10) + digit
            n = n // 10
            
        return abs(original - reversed_num)