
def first_stable_index(nums:list[int],k:int)->int:
    int_list = []
    lat_list = []
    instability_score = []

    if nums:
        int_list = []
        lat_list = []
        for i in range(1,len(nums)):
            int_list = (nums[0:i])
            lat_list = (nums[i-1:])
            print("initial_list",int_list)
            print("lat_list",lat_list)
            instability_score.append(max(int_list)-min(lat_list))
            print(f"instablity score for {int_list} and {lat_list} is :",instability_score)
            int_list = []
            lat_list = []
    instability_score.append(max(nums) - (nums[-1]))

    print("final instability score",instability_score)

    final_answer = 0

    for score in instability_score:
        if score <= k:
            final_answer = k
        else:
            final_answer = -1 

    return final_answer

def main():

    n = int(input("Enter how many numbers you want in a list: "))

    num_list = []

    print(f"Enter {n} numbers one by one")
    for i in range(1,n+1):
        k = int(input(f"Enter number {i} of {n}: "))
        num_list.append(k)

    print(num_list)

    k = int(input("Enter the value of k: "))

    iret = first_stable_index(num_list,k)
    print("Final Answer is: ",iret)



if __name__ == "__main__":
    main()