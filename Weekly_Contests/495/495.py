class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        p =len(s)
        for i in range(0,p):
            if s[i] == s[p - i - 1]:
                return i
            else:
                continue
        return -1
            