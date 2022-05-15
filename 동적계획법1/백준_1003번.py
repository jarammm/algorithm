def fibonacci(n):
    left = [1, 0]
    right = [0, 1]
    if n == 0:
        print(left[0], left[1])
    elif n == 1:
        print(right[0], right[1])
    else:
        for i in range(n-1):
            temp = right[:]
            right[0] += left[0]
            right[1] += left[1]
            left = temp[:]
        print(right[0], right[1])

for j in range(int(input())):
    n = int(input())
    fibonacci(n)
