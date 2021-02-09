def possibleSubstring(s):
    result = []
    for i in range(1, len(s)+1):
        n = len(s)+1-i
        j = 0
        while n > 0:
            result.append(s[j:j+i])
            j+=1
            n-=1
    return result


s = "abcde"
print(possibleSubstring(s))
