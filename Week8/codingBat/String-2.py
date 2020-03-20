# 1
def double_char(s):
    ans = ""
    for i in range(len(s)):
        ans += s[i] + s[i]
    return ans


# 2
def count_code(s):
    cnt = 0
    for i in range(len(s) - 3):
        if s[i:i + 2] == "co" and s[i + 3] == "e":
            cnt += 1
    return cnt


# 3
def count_hi(s):
    cnt = 0
    for i in range(len(s) - 1):
        if s[i:i + 2] == "hi":
            cnt += 1
    return cnt


# 4
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if a.endswith(b) or b.endswith(a):
        return True
    return False


# 5
def cat_dog(s):
    if s.count("cat") == s.count("dog"):
        return True
    else:
        return False


# 6
def xyz_there(s):
    for i in range(len(s) - 2):
        if s[i:i + 3] == "xyz":
            if s[i - 1] != ".":
                return True
    return False
