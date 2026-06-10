class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        rev_num = []
        while n > 0:
            digit = n % 10 # first mistake,instead of // it should be % to get the last digit
            rev_num.append((digit))#second mistake,the int should be converted to string before appending to the list
            n = n  //  10 # third mistake, to remove the last digit we should use floor division (//) instead of regular division (/)

        r_n = "".join(rev_num)# the use of str format above to let the join function work on digits

        return abs(original - (r_n))# fourth mistake, the r_n should be converted back to int before calculating the absolute difference