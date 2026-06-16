class Solution:

    def mirrorFrequency(self, s: str) -> int:
        from collections import Counter

        # Step 1: Count total frequencies across the whole string
        counts = Counter(s)
        processed = set()
        score = 0

        # Step 2: Iterate through each unique character
        for c in counts:
            if c in processed:
                continue

            # Step 3: Find the mirror character using your math
            if c.isdigit():
                m = chr(57 - (ord(c) - 48))
            else:
                m = chr(122 - (ord(c) - 97))

            # Step 4: Add the absolute difference of their frequencies
            score += abs(counts[c] - counts[m])

            # Step 5: Mark both characters as processed to avoid double counting
            processed.add(c)
            processed.add(m)

        return score
