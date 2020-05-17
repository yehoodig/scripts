import sys
import math
from fractions import Fraction
from termcolor import cprint
from sympy import isprime
drops=0
magnitudes=list()
magnitudes.append(0)
def hailstone(n):
    return 3*n+1

def divideBytwo(n):
    return n/2

def collatz(n):
    global drops
    global magnitudes
    if(n % 2 == 0):
        print("n/2=", end='')
        n=divideBytwo(n)
        magnitudes[drops]=magnitudes[drops]+1
    else:
        print("3n+1=", end='')
        n=hailstone(n)
        magnitudes.append(0)
        drops=drops+1
    if(n == 1):
        print(int(n))
        averagedrop=0
        for d in magnitudes:
            averagedrop=averagedrop+d
        averagedrop=averagedrop/(len(magnitudes)-1)
        print(magnitudes)
        print(averagedrop)
        sys.exit()
    print(str(int(n))+", ", end='')
    collatz(n)


oddOnly=False
collapse=False
for i in sys.argv:
        if(i=="odd-only"):
            oddOnly = True
        if(i=="collapse"):
            collapse = True
        if(i.isnumeric()):
            collatz(int(i))
        if(i=="Co"):
            print("2n+1, All odd")
            for n in range(10):
                print(str(int((2*n+1)))+", ", end='')
            print()
            print("3(2n+1)+1, First Hailstone")
            for n in range(10):
                print(str(int((6*n+4)))+", ", end='')
            print()
            print("(3(2n+1)+1)/2, First division")
            for n in range(10):
                print(str(int((6*n+4)/2))+", ", end='')
            print()
            print("(3(2(2n)+1)+1)/2, Even indexed of first division")
            for n in range(10):
                print(str(int(6*n+2))+", ", end='')
            print()
            print("(3(2(2n+1)+1)+1)/2, Odd indexed of first division")
            for n in range(10):
                print(str(int(6*n+5))+", ", end='')
            print()
            print("(3(2(2n)+1)+1)/4, Second division")
            for n in range(10):
                print(str(int(3*n+1))+", ", end='')
            print()
            print("(3(2(2(2n+1))+1)+1)/4, Odd indexed of Second division")
            for n in range(10):
                print(str(int(6*n+4))+", ", end='')
            print()
            sys.exit(0)

print("Starting number: ", end='')
start = int(input())
if(start < 2):
        print("Only positive integers greater than 1 allowed!")
        start=2
print("Ending number: ", end='')
end = int(input())
i=start
while(i <= end):
        n=i
        if(oddOnly and not n%2):
                i=i+1
                continue
        if(isprime(n)):
                cprint("n="+str(n), 'red', end='')
        else:
                cprint("n="+str(n), 'green', end='')
        while(n != 1): 
                print(", ", end='')
                if(n%2):
                        n=int(3*n+1)
                else:
                        if(collapse):
                                p=0
                                while(not n%2):
                                        p=p+1
                                        n=(n/2)
                                if(p > 1):
                                        print("("+str(p-1)+"), ", end='')
                        else:
                                n=(n/2)
                if(isprime(int(n))):
                        cprint(str(int(n)), 'red', end='')
                else:
                        cprint(int(n), 'green', end='')
        i=i+1
        print()

                
