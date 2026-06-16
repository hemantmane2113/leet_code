class Solution:
    def removeZeros(self, n: int) -> int:
        # Converts to string, removes '0', and changes it back to an integer
        return int(str(n).replace('0', ''))