limit = 2000000
is_prime = [True] * limit
is_prime[0] = False
is_prime[1] = False
for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit, i):
            is_prime[j] = False
total = 0
for i in range(limit):
    if is_prime[i]:
        total += i
print(total)