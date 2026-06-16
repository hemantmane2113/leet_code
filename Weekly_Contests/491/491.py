class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vowels = ["a","e","i","o","u"]
        
        s_list  = list(s)

        for i in range(len(s_list) -1 , -1, -1):
            if s_list[i] in vowels:
                del s_list[i] # can also use pop ,but can't use .remove() as .remove() works with value and not index
            else:
                break

        s_new = "".join(s_list)#keep in mind..not to use " ",use ""

        return s_new