
def first_stable_index(nums: list[int], k: int) -> int:
    instability_score = []

    n = len(nums)

    for i in range(n):
        left = nums[0:i+1]     # ✅ include i
        right = nums[i:]       # ✅ start at i

        score = max(left) - min(right)
        instability_score.append(score)

    # find smallest index
    for i, score in enumerate(instability_score):
        if score <= k:
            return i

    return -1

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