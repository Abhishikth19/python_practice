count = 0
number = 1
while count < 10001:
    number = number + 1
    factors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            factors = factors + 1
    if factors == 2:
        count = count + 1
print(number)
