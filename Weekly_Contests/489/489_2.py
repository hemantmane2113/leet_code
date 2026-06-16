from collections import Counter

def solution(arr):
    # Counter creates the dictionary for you automatically
    counts = Counter(arr)
    
    # Using a list comprehension for the filtering
    bulb_on = [key for key, value in counts.items() if value % 2 != 0]
    
    bulb_on.sort()
    return bulb_on


def main():

     bulb = list(map(int,input().split()))

     iret = solution(bulb)

     for i in iret:
          print(*(iret))
     

if __name__ == "__main__":
     main()