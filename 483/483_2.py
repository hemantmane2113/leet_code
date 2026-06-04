# wrong code
# the code is in  progress( will not give final answer )..
# the code is kept to see which part is not working correctly
num = 2103 
digit_list = [] 
while num != 0: 
    digit = num % 10 
    digit_list.append(digit) 
    num = num // 10 

reversed_iterator =reversed(digit_list) 
reversed_list = list(reversed_iterator) 
print(reversed_list) 

num_list = [] 
for i in range(1,len(reversed_list)+1): 
    number = reversed_list[:i] 
    num_list.append(number) 

print(num_list) 

actual_numbers = [] 
temp = 0 
place = 1 

# wrong logic
for i in num_list: 
    for j in i: 
        j = str(j) 
        num = ''.join(j) 
        print(num) 
    actual_numbers.append(num) 
        #num = 0
print(actual_numbers)

# correct logic of just the wrong part

actual_numbers = []

for i in num_list:
    num = 0               # START number here
    for j in i:
        num = num * 10 + j   # BUILD number
    actual_numbers.append(num)  # APPEND once

print(actual_numbers)

# next logic not written