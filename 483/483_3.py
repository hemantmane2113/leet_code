num = 2221


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
    digit = reversed_list[:i]
    num_list.append(digit)

print(num_list)

actual_numbers = []

for digits in num_list:
    number = int("".join(map(str, digits)))
    actual_numbers.append(number)

print(actual_numbers)

largest_even = None

for i in actual_numbers:
    if i % 2 == 0:
        if largest_even is None or i > largest_even:
            largest_even = i

if largest_even is None:
    print("")
else:
    print(str(largest_even))
