from typing import List

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:

        org = nums

        final_list = []

        for i in nums:
            binary_list = []

            while i > 0:
                binary_digit = i % 2
                binary_list.append(binary_digit)
                i = i // 2

            binary_str = "".join(str(x) for x in binary_list)
            final_list.append(binary_str)

        mirror_decimal_list = []

        for binary_num in final_list:
            decimal = 0

            for i, digit in enumerate(reversed(binary_num)):
                if digit == "1":
                    decimal += 2 ** i

            mirror_decimal_list.append(decimal)

        pairs = list(zip(org, mirror_decimal_list))

        pairs.sort(key=lambda x: (x[1], x[0]))

        return [num for num, _ in pairs]