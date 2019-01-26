import re

string = "Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21"

ages = re.findall(r'\d{1,3}', string)

names = re.findall(r'[A-Z][a-z]*',string)

print(ages,names)

final = zip(names,ages)

print(dict(final))
