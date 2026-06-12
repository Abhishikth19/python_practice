n = 1001
total = 1

for side in range(3, n + 1, 2):
    total += 4 * side * side - 6 * (side - 1)

print(total)