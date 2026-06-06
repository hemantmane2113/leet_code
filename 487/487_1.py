
def countMonobit(n: int) -> int:
    if n < 0:
        return 0
        
    score = 1  # This instantly counts the number '0'
    k = 1
    
    # This loop generates and checks the all-1 numbers: 1, 3, 7, 15...
    while (1 << k) - 1 <= n:
        score += 1
        k += 1
        
    return score

# Example usage:
n = 4  
iRet = countMonobit(n)
print(iRet)