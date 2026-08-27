def complete_prime(suf_list, pre_list):
    new_list = suf_list + pre_list
    new_list = set(new_list)
    new_list = list(new_list)
    new_list.sort()

    for i in new_list:
        if i < 2:
            return False
        for j in range(2, i):
            if i % j == 0:
                return False

    return True


def suffix_list(num):
    suffix_list = []
    x = 10
    new_num = -1

    while new_num != num:
        new_num = num % x
        suffix_list.append(new_num)
        x *= 10

    return suffix_list


def prefix_list(num):
    prefix_list = []
    temp = num

    while temp > 0:
        prefix_list.append(temp)
        temp //= 10

    prefix_list.sort()
    return prefix_list


def main():
    number = int(input("Please enter the number: "))
    iRet1 = suffix_list(number)
    iRet2 = prefix_list(number)

    if complete_prime(iRet1, iRet2):
        print(f"{number} is completely prime")
    else:
        print(f"{number} is NOT completely prime")


if __name__ == "__main__":
    main()
