X, P = map(int, input().split())

# Calculate original price
original_price = P / (1 - X / 100)

# Print result rounded to 2 decimal places
print(f"{original_price:.2f}")
