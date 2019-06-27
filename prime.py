N=int(input())
if N<=1000:

  if N>1:
    for i in range(2,N):
      if (N%2)==0:
        print("no")
        break
      else:
        print("yes") 
        break
