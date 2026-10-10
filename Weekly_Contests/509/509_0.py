class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        digit_list = []
      
        final_sum = 0
        largest_digit_list = []
        smallest_digit_list = []

        for i in nums:
            digit_list = []
            while i != 0:
                digit = i % 10
                digit_list.append(digit)
                i = i // 10
                
            largest_digit_list.append(sorted(digit_list)[-1])
            smallest_digit_list.append(sorted(digit_list)[0])
                                      
        digit_range = [a - b for a, b in zip(largest_digit_list, smallest_digit_list)]

        #rev_list = digit_range[::-1]
        
        max_range = max(digit_range)

        for i in range(len(nums)):
            if digit_range[i] == max_range:
                final_sum += nums[i]

        return final_sum
