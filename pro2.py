from itertools import combinations
d,k=map(int,input().split())
n=len(str(d))
lst=list(combinations(str(d),n-k))
lst=sorted(lst)
print(*lst[0],sep='')
         