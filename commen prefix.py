dk=int(input())
ak=[]
for i in range(0,dk):
 de=input()
 ak.append(de)
nn=[]
for i in zip(*ak):
 if(i.count(i[0])==len(i)):
  nn.append(i[0])
 else:
  break
print(''.join(nn))