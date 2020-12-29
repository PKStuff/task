def chocolateFeast(n, c, m):
    count = n // c
    result = count
    left = count
    while left >= m:
        result += (count // m)
        left = (count % m) + (count // m)
        count = left
    return result


n, c, m = 12, 4, 4
chocolateFeast(n, c, m)
