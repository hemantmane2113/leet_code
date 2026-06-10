class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        lower = max(1,n - k)# take only positive number
        upper = n + k
        sum = 0
        for x in range(lower,upper+1):
            if abs(n - x) <= k and (n & x) == 0:
                sum = sum + x
        return sum