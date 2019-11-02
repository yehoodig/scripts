import math
print("Iterations:")
last=int(input())
stype=input()

p=1
def pseries(p, n):
    value=1/(n**p)
    return value

def custom(n):
    value=math.exp(1/n)-math.exp(1/(n+1))
    return value

a=1
r=1
def geometric(a, r, n):
    value=a*(r**(n-1))
    return value

a=(35/((10)**3))#float(input())
r=1/(10**2)#float(input())
def generator(n):
    if stype=="geometric"
       print("a: ")
       a=int(input())
       return geometric(a,r,n)

i=1
sum=0
while(i<=last):
    sum=sum+generator(i)
    print("Term:"+str(i))
    print(" Value:"+str(generator(i))) 
    print(" Sum:"+str(sum))
    i=i+1
