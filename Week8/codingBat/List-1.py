# 1
def first_last6(nums):
    return nums[0] == 6 or nums[len(nums) - 1] == 6


# 2
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


# 3
def reverse3(nums):
    nums.reverse()
    return nums


# 4
def middle_way(a, b):
    array = [a[len(a) / 2], b[len(b) / 2]]
    return array


# 5
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


# 6
def sum3(nums):
    return nums[0] + nums[1] + nums[2]


# 7
def max_end3(nums):
    maxi = nums[0]
    if maxi < nums[len(nums) - 1]:
        maxi = nums[len(nums) - 1]
    for i in range(len(nums)):
        nums[i] = maxi
    return nums


# 8
def make_ends(nums):
    return [nums[0], nums[-1]]


# 9
def make_pi():
    return [3, 1, 4]


# 10
def rotate_left3(nums):
    new_nums = [nums[1], nums[2], nums[0]]
    return new_nums


# 11
def sum2(nums):
    if len(nums) <= 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    return nums[0] + nums[1]


# 12
def has23(nums):
    return 2 in nums or 3 in nums
