def collatz_length(n, memo):
    original = n
    length = 0
    while n != 1:
        if n in memo:
            length += memo[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    memo[original] = length
    return length
memo = {1: 1}
max_length = 0
answer = 0
for i in range(1, 1000000):
    length = collatz_length(i, memo)

    if length > max_length:
        max_length = length
        answer = i
print(answer)
print(max_length)