def concatWithReverse(nums: list[int]) -> list[int]:

    new_nums = []

    for i in range(len(nums)):
        new_nums.append(nums[i])
        """
        though the len of list gets doubled but we don't have to take p = len(nums) * 2 
        because we are just appending the original list and then the reverse of it. 
        so we can just use the original length of the list to iterate through it.
        
        """
      
    for i in range(len(nums)-1, -1, -1):
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