def get_keys(key_name):
    hash_value = 0
    for ch in key_name:
        hash_value+=ord(ch)
    return hash_value

data = [0 for i in range(0, 10)]
def insert_data(value):
    hash_value = get_keys(value)%10
    data[hash_value] = value

def search_value(value):
    hash_value = get_keys(value) % 10
    return data[hash_value]

if __name__ == '__main__':
    while True:
        input_data = input("Enter your value:")
        insert_data(input_data)
        print(search_value(input_data))
        print(data)