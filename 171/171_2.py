
def complete_prime(suf_list,pre_list):

    new_list = suf_list + pre_list
    
    new_list = set(new_list)

    new_list = list(new_list)
    new_list.sort()
    

    for i in new_list:
        for j in range(2,i):
            if i % j == 0:
                return False
    else:
        return True 
    
            
def suffix_list(num):
    suffix_list = []
    
    x = 10
    new_num = 1
    while num != new_num:
        new_num = num % x
        suffix_list.append(new_num)
        x = x * 10
    print("Sorted suffix_list",suffix_list)
    return suffix_list  

def prefix_list(num):
    prefix_list = [num]
    digit_list = []

    while num > 0:
        digit = num % 10

        digit_list.append(digit)

        num = num  // 10

        prefix_list.append(num)

    print(digit_list)
    print(prefix_list)
    prefix_list.pop()
    prefix_list.sort()
    print("sorted prefix_list",prefix_list)
    return prefix_list
        
def main():
    print("Please enter the number")

    number = int(input())

    iRet1 = suffix_list(number)
    iRet2 = prefix_list(number)


    bRet = complete_prime(iRet1,iRet2)
        
    if bRet == True:
        print(f"The {number} is completely prime")
    else:
        print(f"The {number} NOT is completely prime")
    

if __name__ == "__main__":
    main()