def timeInWords(h, m):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]

    if m == 0:
        result = numbers[h] + " o' clock"
    elif m == 15:
        result = "quarter past " + numbers[h]
    elif m in range(1,30):
        if m == 1:
            result = numbers[m] + " minute past " + numbers[h]
        else:
            result = numbers[m] + " minutes past " + numbers[h]
    elif m == 30:
        result = "half past " + numbers[h]
    elif m == 45:
        result = "quarter to " + numbers[h+1]
    elif m in range(31,60):
        result = numbers[60-m] + " minutes to " + numbers[h+1]

    return result
        
print(timeInWords(5,28))
