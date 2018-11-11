from collections import Counter
def func(string1):
  col_count=Counter(string1)
  for k in col_count:
    if col_count[k] > 1:
      print(k)
if __name__ == "__main__":
  string1="geeksforgeeks"
  func(string1)
