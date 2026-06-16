def solution(bulbs):
     
     counts  = {}
     bulb_on = []

     for bulb in bulbs:
          if bulb in counts:
               counts[bulb] += 1
          else:
               counts[bulb] = 1

     print(counts)

     for  key,value in counts.items():
          if value % 2 == 0:
               continue
          else:
               bulb_on.append(key)
     
     bulb_on.sort()
     return bulb_on


def main():

     bulb = list(map(int,input().split()))

     iret = solution(bulb)

     for i in iret:
          print(i,end="")
     

if __name__ == "__main__":
     main()