from typing import List
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        digit_list = []
        while num > 0:
            digit = num % 10
            digit_list.append(digit)
            num = num // 10
       
        num_list = []
        multiple = 1
        for i in range(len(digit_list)):
            new_num = digit_list[i] * multiple
            num_list.append(new_num)
            multiple = multiple * 10
            
            num_list.sort(reverse = True)
            if 0 in num_list:
                num_list.remove(0)
            
        return num_list