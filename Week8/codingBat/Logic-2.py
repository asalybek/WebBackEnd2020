# 1
def make_bricks(small, big, goal):
    if (goal % 5) <= small and (goal - (big * 5)) <= small:
        return True
    return False


# 2
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n == 15 or n == 16:
        return n
    elif 13 <= n <= 19:
        return 0
    return n


# 3

def lone_sum(a, b, c):
    summa = 0
    if a != b and a != c:
        summa += a
    if b != a and b != c:
        summa += b
    if c != a and c != b:
        summa += c
    return summa


# 4
def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c


# 5
def round10(num):
    rounded = num % 10
    if rounded >= 5:
        return num + 10 - rounded
    return num - rounded


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


# 6
def close_far(a, b, c):
    a_b = abs(a - b)
    a_c = abs(a - c)
    b_c = abs(b - c)

    if (a_b <= 1 and a_c >= 2 and b_c >= 2) or (a_c <= 1 and a_b >= 2 and b_c >= 2):
        return True
    return False


# 7
def make_chocolate(small, big, goal):
    if goal >= 5 * big:
        res = goal - 5 * big
    else:
        res = goal % 5
    if res <= small:
        return res
    return -1
