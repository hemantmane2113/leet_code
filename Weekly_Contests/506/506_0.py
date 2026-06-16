class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        flag = False
        digitSum = 0
        squareSum = 0
        digit_list = []
        while n > 0:
            digit = n % 10
            digit_list.append(digit)
            n = n // 10
        for digit in digit_list:
            digitSum = digitSum + digit
            squareSum = squareSum + (digit * digit)
        if squareSum - digitSum >= 50:
            flag = True
        else:
            flag = False
        return flag