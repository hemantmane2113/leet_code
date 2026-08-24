def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True


def complete_prime(num):
    s = str(num)
    length = len(s)

    for k in range(1, length + 1):
        prefix = int(s[:k])
        suffix = int(s[length - k:])

        if not is_prime(prefix) or not is_prime(suffix):
            return False

    return True
