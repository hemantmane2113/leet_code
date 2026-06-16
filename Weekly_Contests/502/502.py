def isAdjacentDiffAtMostTwo(s: str) -> bool:
    #print(s)
    str_list = list(s)
    #print(str_list)
    print(type(str_list[0]))
    flag  = False

    for i in range (0,len(str_list)-1):
        print(f" for {(str_list[i])} - {str_list[i+1]} = ", abs(int(str_list[i]) - int(str_list[i+1])))
        if abs(int(str_list[i]) - int(str_list[i+1])) <= 2:
            flag = True
        else: 
            flag = False
            break # very important to break the loop if we find any adjacent pair that does not satisfy the condition
    return flag




def main():
    num_str = input("Enter the number as a string:  ")


    bRet = isAdjacentDiffAtMostTwo(num_str)

    print(bRet)


if __name__ == "__main__":
    main()

# test for 123,129,191,912