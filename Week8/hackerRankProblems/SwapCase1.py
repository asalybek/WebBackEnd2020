def swap_case(s):
    res = ""
    for i in range(len(s)):
        if s[i].isupper():
            res += ''.join(s[i].lower())
        elif s[i].islower():
            res += ''.join(s[i].upper())
        else:
            res += ''.join(s[i])
    return res