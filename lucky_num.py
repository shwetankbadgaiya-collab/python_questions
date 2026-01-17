a, b = map(int, input().split())

found = False

for num in range(a, b + 1):
    s = str(num)
    lucky = True
    for ch in s:
        if ch != '4' and ch != '7':
            lucky = False
            break
    if lucky:
        print(num, end=" ")
        found = True

if not found:
    print(-1)
