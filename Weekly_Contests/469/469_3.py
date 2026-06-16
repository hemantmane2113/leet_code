class Solution:
    def decimalRepresentation(self, n: int) -> list[int]:
        s = str(n)
        length = len(s)
        
        # Calculate place value using digit position; filter out 0 values
        return [int(digit) * (10 ** (length - 1 - i)) for i, digit in enumerate(s) if digit != '0']

        """
        final_list = []
        for i,digit in enumerate(s):
            if digit != '0':
                place_value = int(digit) * (10 ** (length - 1 - i))
                final_list.append(place_value)
        return final_list
        
        """

