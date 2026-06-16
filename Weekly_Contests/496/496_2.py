class Solution:

    def mirrorFrequency(self, s: str) -> int:
        score = 0
        freq = {}
        seen = set()  # Track pairs we already calculated

        # Step 1: Count total frequencies of all characters in the string
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Step 2: Calculate the score based on unique characters
        for i in freq:
            if i in seen:
                continue

            # For digits
            if i.isdigit():
                mirror_digit = chr(57 - (ord(i) - 48))

                current_freq = freq[i]
                mirror_freq = freq.get(mirror_digit, 0)

                score += abs(current_freq - mirror_freq)

                # Mark both as seen so we don't count them again
                seen.add(i)
                seen.add(mirror_digit)

            # For letters
            elif i.islower():
                mirror_letter = chr(122 - (ord(i) - 97))

                current_freq = freq[i]
                mirror_freq = freq.get(mirror_letter, 0)

                score += abs(current_freq - mirror_freq)

                # Mark both as seen so we don't count them again
                seen.add(i)
                seen.add(mirror_letter)

        return score
