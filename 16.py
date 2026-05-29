numbers = "10 20 30 40 50"
total = sum(int(num) for num in numbers.split())

answer = str(total)[:10]

print(answer)