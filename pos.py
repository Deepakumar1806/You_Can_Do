dk,ak=map(str,input().split())
e=0
if len(dk)>len(ak):
   dk,ak=ak,dk
r=0
while r<len(dk):
   e+=(ord(ak[r])-ord(dk[r]))
   r+=1
for r in range(r,len(ak)):
   e+=ord(ak[r])-ord('a')+1
print(e)