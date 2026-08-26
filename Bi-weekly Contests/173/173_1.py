strr = "hemant"
k = 2

new_str_1 = ''
for i in range(k):
    new_str_1 += strr[i]

print(new_str_1)

#new_str_1_reversed = reversed(new_str_1)
#print(new_str_1_reversed)
print("".join(reversed(new_str_1)))


new_str_2 = strr[k:]
print(new_str_2)

final_word = new_str_1[::-1] + new_str_2
print(final_word)
    



