def findBestBox(capacity: list[int], itemSize: int) -> int:
    min_capacity = float('inf')
    best_index = -1
    
    for i, cap in enumerate(capacity):
        # Check if the box is big enough
        if cap >= itemSize:
            # Check if this box has a strictly smaller capacity than our current choice
            if cap < min_capacity:
                min_capacity = cap
                best_index = i
                
    return best_index
