from typing import List
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        minimum_time = float('inf')
        for task in tasks:
            for i in range(len(task)):
                minimum = task[0] + task[1]
                if minimum < minimum_time:
                    minimum_time = minimum