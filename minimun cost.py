dk,ak=input().split()
ar=abs(len(ak)-len(dk))
for y in range(len(dk)):
  if(len(ak)==1 and ak[y] in dk):
    break
  if(dk[y]!=ak[y]):
    ar+=1
print(ar)    