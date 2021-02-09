def locationarray(index, identity):
    i = 0
    while i < len(index):
        if index[i] != identity[i]:
            element = identity[i]
            del identity[i]
            identity.insert(index[i], element)
        i += 1
    return identity


index = [0, 1, 2, 1, 0]
identity = [0, 1, 2, 3, 4]
print(locationarray(index, identity))
