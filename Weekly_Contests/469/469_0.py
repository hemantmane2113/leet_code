
from typing import List
class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        n_s = list(str(n))
        multiple = 1
        num_list = []
        for i in range(len(n_s)-1,-1,-1):
            new_num = int(n_s[i]) * multiple
        
            num_list.append(new_num)
            multiple = multiple * 10
            num_list.sort(reverse = True)
            final_list = num_list
            if 0 in final_list:
                final_list.remove(0)

        return final_list