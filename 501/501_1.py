
def concatWithReverse(nums: list[int]) -> list[int]:
   
    p = len(nums) * 2
    new_nums = []

    for i in range(0,(p+1)//2):
        new_nums.append(nums[i])


    for i in range((p)//2 -1 ,-1,-1):
        new_nums.append(nums[i])

    
    return new_nums

      
def main():
    print('You have to  enter the list of given length')
    num = int(input("Enter the length of the list: "))
    num_list = []
    for i in range(1, num+1):
        k = int(input(f"Enter number {i} of {num}: "))
        num_list.append(k)
    print(num_list)

    iRet = concatWithReverse(num_list)
    print(iRet)






if __name__ == "__main__":
    main()