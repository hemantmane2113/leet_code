class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        from collections import Counter
        digit_list = []
        score = 0
        while n > 0:
            digit = n % 10          # Get the last digit
            digit_list.append(digit)
            n //= 10

        digit_counter = Counter(digit_list)

        for value,freq in digit_counter.items():
            score = value * freq + score

        return score
            
        
            
        