my_list = ["geeks", "geeg", "keek", "practice", "aa"]

str = "eegsk"

result = list(filter(lambda x: sorted(x) == sorted(str), my_list))

print(result)
