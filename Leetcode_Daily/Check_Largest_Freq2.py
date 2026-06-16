def CheckLargestFreq(Arr):
    #step1 : make dictionary of element:frequency
    Freq_check = {}
    for i in Arr:
        Count = 0

        for j in Arr:
              if i == j:
                Count = Count + 1
        Freq_check[i] = Count

    print("Dict of max_freqs is:",Freq_check)

    # step2 : Count Freq of each freq eg. {value from above dict will be a key here:freq}
    value_counts = {}

    for value in Freq_check.values():
        if value in value_counts:
            value_counts[value] = value_counts[value] + 1
        else:
            value_counts[value] = 1

    print("Value_Count",value_counts)

    #step3: Count MAXIMUM frequency of each key from above dict
    Max_Freq = 0

    for key in value_counts.keys():
        if key > Max_Freq:
            Max_Freq = key

    print("Maximum frq is:",Max_Freq)


    #step4: Calculate sum of all keys having maximum freq
    Max_Freq_Sum = 0

    for value in Freq_check.values():
        if Freq_check[value] == Max_Freq:
            Max_Freq_Sum = Max_Freq_Sum + value

    print("Sum of max freq is: ",Max_Freq_Sum)

    return Max_Freq_Sum


def main():

    print("Enter how many elements do you want in list: ")
    n = int(input())

    print(f"Enter the {n} elements one by one: ")
    num_list = []
    for i in range(1,n+1):
        print(f"Enter num {i} of {n}: ")
        num = int(input())
        num_list.append(num)

    print(num_list)

    iRet = CheckLargestFreq(num_list)
    print(f"The sum of   highest frequencies is {iRet}")


if __name__ == "__main__":
    main()

