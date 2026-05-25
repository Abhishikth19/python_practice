n = 600851475143
factor = 2
largest = 1
while factor * factor <= n:
    if n % factor == 0:
        largest = factor
        n = n // factor
    else:
        factor = factor + 1
if n > largest:
    largest = n
print(largest)