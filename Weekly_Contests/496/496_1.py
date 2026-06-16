class Solution:
    def mirrorFrequency(self, s: str) -> int:
        score = 0
        s_list = list((s))
        seen = set()
        freq = {}
        
        for i in s_list:
            #for digits
            if i.isdigit(): 
                mirror_digit = chr(57 - (ord(i) - 48))
                # current digit in list
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
                    
                if mirror_digit not in s_list:
                    if mirror_digit in freq:
                        freq[mirror_digit] += 1
                    else:
                        freq[mirror_digit] = 1
                        
                # 3. Fetch frequencies safely (use .get() to avoid KeyError if missing)
                current_freq = freq[i]
                mirror_freq = freq.get(mirror_digit, 0)    
                
                    
                score += abs(current_freq-mirror_freq)
              

            #for chars
            elif i.islower():
                mirror_letter = chr(122 - (ord(i) - 97))

                #for current chars
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
                    
                if mirror_letter not in s_list:
                    if mirror_letter in freq:
                        freq[mirror_letter] += 1
                    else:
                        freq[mirror_letter] = 1
                        
                #Fetch frequencies safely (use .get() to avoid KeyError if missing)
                current_freq = freq[i]
                mirror_freq = freq.get(mirror_letter, 0)  
                
                score += abs(current_freq - mirror_freq)
                
            else: 
                continue
        return score
      
        