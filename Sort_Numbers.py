A, B, C = map(int, input().split())

original = [A, B, C]

sorted_nums = sorted(original)

for num in sorted_nums:
    print(num)

print()  

for num in original:
    print(num)
