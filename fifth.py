num=20
while True:
  divisible=True
  for i in range(1,21):
    if num%i!=0:
      divisible=False
      break
  if divisible:
   print(num)
   break
  num=num+20
