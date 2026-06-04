def findBestBox(capacity: list[int], itemSize: int) -> int:
    min_capacity = float('inf')
    best_index = -1
    
    for i, cap in enumerate(capacity):
        if cap >= itemSize:
            if cap < min_capacity:
                min_capacity = cap
                best_index = i
            else:
                continue # Do nothing, move to next iteration
        else:
            continue # Do nothing, move to next iteration
                
    return best_index