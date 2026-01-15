n = input().strip()

# reverse number and remove leading zeros
rev = n[::-1].lstrip('0')

# if all digits were zero (edge case like "0")
if rev == "":
    rev = "0"

print(rev)

# palindrome check
if n == n[::-1]:
    print("YES")
else:
    print("NO")
