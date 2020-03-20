a = int(input())
array = [int(i) for i in input().split()]
tuplexi = tuple(array)
print(tuplexi.__hash__())
