string1 = 'geeksforgeeks'
string2 = 'forgeeksgeeks'

def anagram(string1, string2):

    if len(string1) != len(string2):
        return False
    count = [0] * 26
    for i in range(0,len(string1)):
        count[ord(string1[i])-96]+=1
        count[ord(string2[i])-96]-=1
    
    for i in count:
        if i != 0:
            return False
    return True


ans = anagram(string1, string2)
print(ans)
