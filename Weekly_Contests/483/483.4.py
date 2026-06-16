class Solution:
    def largestEvenNumber(self, s: str) -> str:
        index_of_last_two = s.rfind('2')
        
        if index_of_last_two == -1:#not found
            return ""
        
        return s[:index_of_last_two + 1]
