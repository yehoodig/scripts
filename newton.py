# Implementation of Newton's Method, on n-th order roots.
# James McConnel
# Sun Jul 28 21:06:18 2019

print("Root Order: ")
exp = float(input())

print("Root of: ")
r = float(input())

print("Guess: ")
newton = float(input())

print("Iterations: ")
i = int(input())

while(i):
   x1 = newton
   x2a = (x1**exp) - r       # f(x)
   x2b = (exp*x1**(exp - 1)) # f'(x)
   newton = x1 - (x2a/x2b)
   print(newton)
   i = i -1

