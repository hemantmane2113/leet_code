class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minimum_capacity = float("inf")
        best_index = -1
        i = 0

        while len(capacity)>i:
            if capacity[i] >= itemSize:
                if capacity[i] < minimum_capacity:
                    minimum_capacity = capacity[i]
                    best_index = i
            i += 1
        return best_index