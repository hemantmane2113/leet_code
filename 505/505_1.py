class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        lower = max(1, n - k)
        upper = n + k
        
        # 'mask' represents all valid bit positions that are 0 in n
        # We limit the mask length to the bit length of upper
        mask = (~n) & ((1 << upper.bit_length()) - 1)
        
        total_sum = 0
        submask = mask
        
        # Iterate only through the submasks of ~n
        while submask > 0:
            if lower <= submask <= upper:
                total_sum += submask
            # Standard bitwise trick to get the next submask down
            submask = (submask - 1) & mask
            
        return total_sum