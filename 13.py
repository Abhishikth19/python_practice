ones = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def number_to_words(n):
    if n == 1000:
        return "onethousand"
    if n >= 100:
        hundred_part = ones[n // 100] + "hundred"
        if n % 100 != 0:
            return hundred_part + "and" + number_to_words(n % 100)
        else:
            return hundred_part
    if n >= 20:
        ten_part = tens[(n // 10) * 10]
        if n % 10 != 0:
            return ten_part + ones[n % 10]
        else:
            return ten_part
    return ones[n]
total = 0
for i in range(1, 1001):
    word = number_to_words(i)
    total += len(word)
print(total)