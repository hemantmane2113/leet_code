def findValidElements(nums: list[int]) -> list[int]:
    """
    The number in a list must satisfy atleast one of the below conditions:

    It is strictly greater than every element to its left.
    It is strictly greater than every element to its right.

    """
    #final_list = []
    valid_indices = set()
    p = len(nums)

    
    #final_list.append(nums[0])
    

    for i in range(0,p):# first element gets automatically added to the final list because it is greater than all elements to its left (there are no elements to its left)
        for j in range(0,i):
            if nums[i] <= nums[j]:
                break
        else:
            #final_list.append(nums[i])
            valid_indices.add(i)

    for i in range(p-1,-1,-1):# last element gets automatically added to the final list because it is greater than all elements to its right (there are no elements to its right)
        for j in range(i+1,p):
            if nums[i] <= nums[j]:
                break
        else:
            #if nums[i] not in final_list:
                #final_list.append(nums[i])
            valid_indices.add(i)

    # if len(nums) > 1:
    #     #final_list.append(nums[-1])
    

        
    return [nums[i] for i in sorted(valid_indices)]


def main():
    print("Enter the numbers into the array of desired length")

    k = int(input("How many numbers you want in a list: "))
    num_list = []
    for i in range(1,k+1):
        x = int(input(f"Enter the num {i} of {k}: "))
        num_list.append(x)
    print(num_list)

    iret = findValidElements(num_list)
    print(iret)




if __name__ == "__main__":
    main()