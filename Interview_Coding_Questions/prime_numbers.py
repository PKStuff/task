def isPrime(number):
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        return number
    return prime

print(list(filter(lambda x: x, list(map(isPrime, range(100))))))
