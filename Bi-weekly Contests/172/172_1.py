num_list = [2,3,4,5,6,7]

count = 0
def counter():
    global count
    count = count + 1

def del_more_than_three(listt):
    del num_list[:3]
    counter()
    return num_list

while len(num_list)<= 3:
    new_list = del_more_than_three(num_list)
    
if len(num_list) > 3:
    num_list.clear()
    counter()

print()
