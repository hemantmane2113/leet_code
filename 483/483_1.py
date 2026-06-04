
number = str(221)
number_1 = int(221)

num_list = []
temp = 0
place = 1

max = 0
required_number = 0
while number_1 != 0:
    digit = number_1 % 10

    temp = digit * place + temp

    num_list.append(temp)
    place = place * 10

    number_1 =  number_1 // 10
    
print(num_list)

for i in num_list:
    if i % 2 == 0:
        if i > max:
            required_number = i
    else:
        required_number = ''

print(required_number)


