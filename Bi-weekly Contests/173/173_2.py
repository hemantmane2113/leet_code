strr = 'hemant'
k = 2

list_of_words = list(strr)
print(list_of_words)

empty_list = []
for i in range(0,k):
    empty_list.append(list_of_words[i])

new_list = list_of_words[k:]
empty_list.reverse()
print(empty_list)
print(new_list)

final_list = empty_list + new_list

print(final_list)

final_word = "".join(final_list)
print(final_word)
