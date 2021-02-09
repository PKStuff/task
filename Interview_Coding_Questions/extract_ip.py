"""
This is my IP address 10.10.20.189 on network 2020.1.1 and also 192.168.0.1
"""

def extractIP(s1):
    s1 = s1.split()
    for string in s1:
        if string.count('.') == 3:
            print(string)


s1 = "This is my IP address 10.10.20.189 on network 2020.1.1 and also 192.168.0.1"
extractIP(s1)