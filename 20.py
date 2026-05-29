import math

number = math.factorial(100)

digit_sum = sum(int(digit) for digit in str(number))

print(digit_sum)