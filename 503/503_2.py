from collections import Counter

def LimitOccurance(listt,k):
    print(listt)
    print(k)

    final_list = []
    counter = 0
    frequency = Counter(listt)
    print(frequency)
    for item,count in frequency.items():
        print(f"Number:{item} has frequency count of {count}")
    
    for i in listt:
        for item,count in frequency.items():
            if i == item:
                if k > counter:
                    final_list.append(i)
        





def main():
    print("You have to enter the numbers in a list")
    num_list = []
    x = int(input("How many numbers do you want to enter: "))
    for i in range(1,x+1):
        num = int(input(f"Enter num {i} of {x}:  "))
        num_list.append(num)
    print(num_list)
    listt = (sorted(num_list))
    
    k = int(input("Enter the value of limit: "))

    iRet = LimitOccurance(listt,k)

    #print(f"Final answer is: {iRet}")


if __name__ == "__main__":
    main()