n = int(input())
A = list(map(int, input().split()))

total = 0
for x in A:
    total += x

print(abs(total))
