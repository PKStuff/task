def index(values, weights, W):
    result = []
    sorted_index = []
    max_pos_val = 0
    max_pos_weigth = 0

    for i in range(0,len(values)):
        result.append(values[i]/weights[i])
    
    for i in sorted(result):
        sorted_index.append(result.index(i))

    for i in sorted_index:
        if W > max_pos_weigth and W >= (max_pos_weigth + weights[i]):
            max_pos_weigth += weights[i]
            max_pos_val += values[i]
    
    return max_pos_val


if __name__ == '__main__':
    values = list(map(int,input("Enter the values:").split()))
    weights = list(map(int,input("Enter the weights:").split()))
    W = int(input("Enter the Capacity:"))
    result = index(values, weights, W)
    print(result)

