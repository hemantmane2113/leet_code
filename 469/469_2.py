class Solution:
    def decimalRepresentation(self, n: int) -> list[int]:
        if n == 0:
            return []
            
        final_list = []
        multiple = 1
        
        while n > 0:
            digit = n % 10
            if digit != 0:
                final_list.insert(0, digit * multiple)
            multiple *= 10
            n //= 10
            
        return final_list
