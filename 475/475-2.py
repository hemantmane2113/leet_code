from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        positions = defaultdict(list)
        for i, v in enumerate(nums):
            positions[v].append(i)

        best_span = float('inf')
        for inds in positions.values():
            if len(inds) >= 3:
                for t in range(len(inds) - 2):
                    span = inds[t + 2] - inds[t]
                    if span < best_span:
                        best_span = span

        if best_span == float('inf'):
            return -1
        return 2 * best_span

def main():
    # read space-separated integers on one line, e.g.:
    # 1 2 1 1 3
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        print(-1)
        return

    nums = list(map(int, data))
    s = Solution()
    print(s.minimumDistance(nums))

if __name__ == "__main__":
    main()
