class Solution:
    def mirrorDistance(self, n: int) -> int:
        # str(n)[::-1] converts to string and reverses it
        return abs(n - int(str(n)[::-1]))