a = int(input())

for x in range(2, a + 1):
    if a % x == 0:
        print(x)
        break

