ini,en=map(int,input().split())
for i in range(ini+1,en,1):
      if(i>1):
        for x in range(2,i):
          if(i%x==0):
             break
        else:
           print(i,end=" ")
