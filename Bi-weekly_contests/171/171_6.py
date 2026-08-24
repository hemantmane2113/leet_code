class Solution:
    def completePrime(self, num: int) -> bool:

        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        s = str(num)
        length = len(s)

        for k in range(1, length + 1):
            prefix = int(s[:k])
            suffix = int(s[length - k:])

            if not is_prime(prefix) or not is_prime(suffix):
                return False

        return True
