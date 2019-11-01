import math
print("Series type or Maclaurin Expansion function: ")
series_type=input()
print(series_type)
print("n= ")
i=int(input())
print("Iterations: ")
last=int(input())

p=1
def pseries(p, n):
	value=1/(n**p)
	return value
	

#x=math.pi/2
x=math.pi/4
#x=0.5
def mac_sine(x, n):
	value=((-1)**n)*((x**(2*n+1))/math.factorial(2*n+1))
	return value
	

def mac_cosine(x, n):
	value=((-1)**n)*((x**(2*n))/math.factorial(2*n))
	return value

a=1
r=1
def geometric(a, r, n):
	value=a*(r**(n-1))
	return value

if series_type=="p":
	print("p-value: ")
	p=eval(input())
elif series_type=="geometric":
	print("a-value: ")
	a=eval(input())
	print("r-value: ")
	r=eval(input())
elif series_type=="sine" or series_type=="cosine" or "tangent":
	print("x-value: ")
	x=eval(input())
	print(x)


def generator(n):
	if series_type=="p":
		return pseries(p,n)
	if series_type=="geometric":
		return geometric(a,r,n)
	if series_type=="sine":
		return mac_sine(x,n)	
	if series_type=="cosine":
		return mac_cosine(x,n)
	if series_type=="tangent":
		return (mac_sine(x,n)/mac_cosine(x,n))
	if series_type=="custom":
		return custom(n)
	
try:
	sum=0
	while(i<=last):
		sum=sum+generator(i)
		print("Term:"+str(i))
		print(" Value:"+str(generator(i)))
		print(" Sum:"+str(sum))
		i=i+1
except OverflowError:
	print("Value or Sum exceeded the limits of the data type")

	
