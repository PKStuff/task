
def convert_to_decimal(number):
    index = 0
    final_result = 0
    while number > 0:
        digit = number%10
        final_result+=(digit*2**index)
        index+=1
        number//=10
    return final_result


print(convert_to_decimal(100001))