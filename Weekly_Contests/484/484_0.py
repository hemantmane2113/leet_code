class Solution:
    def residuePrefixes(self, s: str) -> int:
        residue_count = 0
        s_list = list(s)
        l = len(s_list)
        for i in range(0,l):
            if len(s_list[0:i + 1]) % 3 == len(set(s_list[0:i + 1])):
                residue_count += 1
        return residue_count