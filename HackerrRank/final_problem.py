def flip(input, k):
    first = input[:k]
    resp = ''.join('1' if x=='0' else '0' for x in input[k:])
    return first + resp

def func(input):
    expected = input
    actual = '0'*len(input)
    i = 0
    count = 0
    if expected == actual:
        return 0
    else:
        while i<len(input):
            if expected[i] == actual[i]:
                pass
            else:
                actual = flip(actual, i)
                count+=1
                if expected == actual:
                    break
            i+=1
    return count

if __name__ == '__main__':
    input = '10101'
    resp = func(input)
    print(resp)
