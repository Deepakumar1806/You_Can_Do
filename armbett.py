lower1,upper1=map(int,input().split())
for nu in range(lower1, upper1 + 1):
  order1 = len(str(nu))
  sum1 = 0
  temp=nu
  while temp > 0:
    digit = temp % 10
    sum1 += digit ** order1
    temp //= 10
    if nu == sum1:
      print(nu)