from typing import List

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        
        # Helper function to reverse bits mathematically (No strings used)
        def get_reflected_val(n: int) -> int:
            reflected = 0
            while n > 0:
                # Shift reflected left, and inject the last bit of n
                reflected = (reflected << 1) | (n & 1)
                n >>= 1  # Divide n by 2 (bit shift right)
            return reflected

        # Sort directly using a key function. 
        # Timsort handles the rest with minimum memory overhead.
        return sorted(nums, key=lambda x: (get_reflected_val(x), x))
