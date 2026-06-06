def countMonobit(n: int) -> int:
    
    bit_list = []
             
    for i in range(0,n+1):
        if i == 0:
            bit_list.append([0])
            continue

        current_number = []
        temp = i
        while temp > 0:
            remainder = temp % 2
            current_number.append(remainder)
            temp = temp // 2
        bit_list.append(current_number[  ::-1])
    
    score = 0
    for i in bit_list:
         if all(x == i[0] for x in i):
            score += 1     
                
    return score

# Example usage:
n = 4  
iRet = countMonobit(n)
print(iRet)