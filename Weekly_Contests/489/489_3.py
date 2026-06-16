class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
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