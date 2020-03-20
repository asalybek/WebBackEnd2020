# 1
def hello_name(name):
    return "Hello " + name + "!"


# 2
def make_out_word(out, word):
    return out[:2] + word + out[2:]


# 3
def first_half(s):
    return s[:len(s) // 2]


# 4
def non_start(a, b):
    return a[1:] + b[1:]


# 5
def make_abba(a, b):
    return a + b + b + a


# 6
def extra_end(s):
    res = s[len(s) - 2:len(s)]
    return res + res + res


# 7
def without_end(s):
    return s[1:len(s) - 1]


# 8
def left2(s):
    return s[2:len(s)] + s[:2]


# 9
def make_tags(tag, word):
    return "<" + tag + ">" + word + "</" + tag + ">"


# 10
def first_two(s):
    if len(s) < 2:
        return s
    return s[:2]


# 11
def combo_string(a, b):
    if len(b) < len(a):
        return b + a + b
    return a + b + a
