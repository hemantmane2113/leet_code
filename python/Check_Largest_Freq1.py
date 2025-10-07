def CheckLargestFreq(Arr):
    
    Freq_check = {}
    for i in Arr:
        Count = 0
        for j in Arr:
            
            if i == j:
                Count = Count + 1
        Freq_check[i] = Count

    print(Freq_check)
    
    max_key = max(Freq_check,key = Freq_check.get)
    max_value = Freq_check[max_key]
    
    return max_key,max_value


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
    print(f"The number {iRet[0]} has the highest frequency of {iRet[1]}")




if __name__ == "__main__":
    main()

"""
Sure! Let’s break down this code line by line so it’s crystal clear.


eg. scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

Here, scores is a dictionary with keys as names and values as their scores.

1️⃣ Find the key with the maximum value:

   -> max_key = max(scores, key=scores.get)

    
        max() finds the largest element in an iterable.

        scores by itself iterates over the keys: 'Alice', 'Bob', 'Charlie'.

        key=scores.get tells max() to compare the values of the keys, not the keys themselves.

        So what happens step by step:
        Key	Value            (scores.get(key))
        Alice	                   85
        Bob	                       92
        Charlie	                   78

        max() compares 85, 92, 78 (values)

        Finds 92 → corresponds to key 'Bob'

        So max_key = 'Bob'

2️⃣ Get the maximum value:

    -> max_value = scores[max_key]

        Now that we know max_key = 'Bob',

        scores[max_key] → scores['Bob'] → 92

        So max_value = 92

3️⃣ Print result:

    -> print(max_key, max_value)  # Output: Bob 92

        Prints the key and its maximum value.

✅ Summary:

max(dictionary, key=dictionary.get) → finds key with the largest value

dictionary[key] → gets the value for that key


"""

