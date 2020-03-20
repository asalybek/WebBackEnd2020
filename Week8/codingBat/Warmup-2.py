# 1
def string_times(s, n):
    part = s
    s = ""
    for i in range(n):
        s += part
    return s


# 2
def front_times(s, n):
    part = s
    s = ""
    for i in range(n):
        s += part[0:3]
    return s


# 3
def string_splosion(s):
    ans = ""
    for i in range(len(s)):
        ans += s[:i + 1]
    return ans


# 4
def array_front9(nums):
    for i in range(len(nums)):
        if nums[i] == 9:
            if i == 0 or i == 1 or i == 2 or i == 3:
                return True
    return False


# 5
def last2(s):
    sub = s[len(s) - 2:len(s)]
    cnt = 0
    for i in range(len(s) - len(sub)):
        if s[i:i + len(sub)] == sub:
            cnt += 1
    print(cnt)


# 6
def array123(nums):
    arr_string = ""
    for i in range(len(nums)):
        arr_string += str(nums[i])
    if '123' in arr_string:
        return True
    else:
        return False


# 7
def string_bits(s):
    i = 0
    res = ""
    while len(s) > 0 and i < len(s):
        res += s[i]
        i += 2
    return res


# 8
def array_count9(nums):
    cnt = 0
    for i in nums:
        if i == 9:
            cnt += 1
    return cnt


# 9
def string_match(a, b):
    short = min(len(a), len(b))
    cnt = 0
    for i in range(short - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            cnt = cnt + 1
    return cnt
