from typing import List
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if num % 2 == 0:
                result |= num # result = result | num
        
        return result

"""
Computers store all data—including decimal integers—in binary (0s and 1s) inside your system's memory.
When you use a bitwise operator like |, Python looks directly at those internal binary bits, 
performs the operation, and then translates the result back into a decimal number for you to read.

graph TD
    A["You type: 4 | 2"] --> B["1. Python looks at the memory where 4 and 2 are stored as binary (0100 and 0010)"]
    B --> C["2. CPU processes the Bitwise OR on those bits (0100 | 0010 = 0110)"]
    C --> D["3. Python converts the binary result (0110) back into a decimal integer (6)"]
    D --> E["Output: 6"]

"""