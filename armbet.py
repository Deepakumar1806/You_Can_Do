lower,upper=map(int,input().split())
for nu in range(lower, upper + 1):
  order = len(str(nu))
  sum = 0
  temp=nu
  while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
    if nu == sum:
      print(nu)