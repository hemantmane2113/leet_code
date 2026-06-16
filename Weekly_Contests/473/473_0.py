class Solution:
    def removeZeros(self, n: int) -> int:
        num_list = []
 
        while n > 0:
            digit = n % 10
            if digit != 0:
                num_list.append(digit)
            n = n // 10
            
        num_list = num_list[::-1]# also num_list.reverse() can be used  
        #num_list.reverse()
        
    
        result = 0
        for digit in num_list:
            result = result * 10 + digit
        return result