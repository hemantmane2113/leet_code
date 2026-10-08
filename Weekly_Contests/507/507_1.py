class Solution:
    def maxDistance(self, moves: str) -> int:
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        blanks = 0
        
        for i in range(len(moves)):
            if moves[i] == 'L':
                x2, y2 = x2 - 1, y2
            elif moves[i] == 'R':
                x2, y2 = x2 + 1, y2
            elif moves[i] == 'U':
                x2, y2 = x2, y2 + 1
            elif moves[i] == 'D':
                x2, y2 = x2, y2 - 1
            elif moves[i] == '_':
                blanks += 1  # Save the choices for the end
                    
        # Max distance = net certain distance + total flexible choices
        return abs(x1 - x2) + abs(y1 - y2) + blanks
