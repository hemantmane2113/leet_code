class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        rev_num = []
        while n > 0:
            digit = n % 10
            rev_num.append(str(digit))
            n = n  //  10

        r_n = "".join(rev_num)

        return abs(original - int(r_n))