from typing import List
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        time = [sum(listt) for listt in tasks]
        return min(time)