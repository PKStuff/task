def isValid(s:str):
    if len(s) < 2:
        return False
    st = []
    for ch in s:
        if ch in ['(', '{', '[']:
            st.append(ch)
        else:
            if len(st) > 0:
                if (ch == ')' and st[-1] == '(') or (ch == '}' and st[-1] == '{') or (ch == ']' and st[-1] == '[') :
                    st.pop()
                else:
                    if len(st) == 0:
                        return True
                    else:
                        return False
            else:
                return False
    if len(st) != 0:
        return False
    return True

s = "()"

print(isValid(s))
