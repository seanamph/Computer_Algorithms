import random

def RSum(a, n):
    if(n<=0) :
        return 0
    return RSum(a,n-1)+a[n]

x = random.randint(0, 200)
a = []
for i in range(0,x,1):
    a.append(random.randint(0, 200))

print(RSum(a,len(a)-1))