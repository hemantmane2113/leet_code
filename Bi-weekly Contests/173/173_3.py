
def reversed_partial_string_from_beginning(s:str,k:int)->str:
    
    final_word = s[:k][::-1]+s[k:]

    return final_word

def main():
    print("Enter the string")
    strr = input()

    print("Enter the number of letters you want to get reversed from the begining of the string")
    number = int(input())

    reversed_string = reversed_partial_string_from_beginning(strr,number)

    print(f"The reversed string format of '{strr}' with {number} of its inital letters reversed is: '{reversed_string}' ")


if __name__ == "__main__":
    main()