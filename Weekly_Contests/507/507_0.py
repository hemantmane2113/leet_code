class Solution:
    def maxDistance(self, moves: str) -> int:
        
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        
        for i in range(len(moves)):
            if moves[i] == 'L':
                x2, y2 = x2 - 1, y2 - 0  # L changes horizontal (x)
            elif moves[i] == 'R':
                x2, y2 = x2 + 1, y2 - 0  # R changes horizontal (x)
            elif moves[i] == 'U':
                x2, y2 = x2 - 0, y2 + 1  # U changes vertical (y)
            elif moves[i] == 'D':
                x2, y2 = x2 - 0, y2 - 1  # D changes vertical (y)
            elif moves[i] == '_':
                if i > 0:
                    if moves[i-1] == 'L':
                        x2, y2 = x2 - 1, y2 - 0
                    elif moves[i-1] == 'R':
                        x2, y2 = x2 + 1, y2 - 0
                    elif moves[i-1] == 'U':
                        x2, y2 = x2 - 0, y2 + 1
                    elif moves[i-1] == 'D':
                        x2, y2 = x2 - 0, y2 - 1
                else:
                    # First character is '_', cannot look back
                    x2, y2 = x2, y2 
                    
        return abs(x1 - x2) + abs(y1 - y2)
