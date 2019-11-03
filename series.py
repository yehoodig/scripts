import math
#Maclaurin expansion generators
x=math.pi/4
def mac_sine(n, x):
        value=((-1)**n)*((x**(2*n+1))/math.factorial(2*n+1))
        return value

def mac_cosine(n, x):
        value=((-1)**n)*((x**(2*n))/math.factorial(2*n))
        return value

#series generators
def p_series(n, p):
        value=1/(n**p)
        return value
        
def geometric(n, a, r):
        value=a*(r**(n-1))
        return value
generators={"geometric":geometric, "p-series":p_series, "sine":mac_sine, "cosine":mac_cosine}

def sum_series(term_index, n, generator):
    sum=0
    try:
        while(term_index<=n):
            sum=sum+generator(term_index)
            term_index=term_index+1
        return sum
    except OverflowError:
        return sum

def sequence(term_index, n, generator):
    start=term_index
    while(term_index<=n):
        print(str(sum_series(start, term_index, generator))+", ", end='')
        term_index=term_index+1
    print()

command=0
print("For a list of commands type: help")
while(command!="exit"):
    print("$:", end='')
    command = input()
    i=0
    n=0
    x=0
    a=0
    r=0
    p=0
    gen=0
    if(command=="help"):
        print("help: Prints this message")
        print("sum: Prints the sum of a series")
        print("sequence: Prints a sequence of partial sums for a series")
        print("list: Lists the generators available.")
        command=0
        continue
    if(command=="list"):
        print(list(generators.keys()))
        continue
    if(command=="exit"):
        break
    if(command=="sum" or command=="sequence"):
        print("Series type: ", end='')
        stype = input()
        print("n=:", end='')
        n=int(input())
        print("Iterations: ", end='')
        i=int(input())
        if(stype=="power" or stype=="maclaurin"):
           print("Function: ", end='')
           f=input()
           print("x-value: ", end='')
           x=eval(input())
           gen=lambda n: generators[f](n, x)
        if(stype=="p_series"):
           print("p-value: ", end='')
           p=eval(input())
           gen=lambda n: generators[stype](n, p)
        if(stype=="geometric"):
           print("a-value: ", end='')
           a=eval(input())
           print("r-value: ", end='')
           r=eval(input())
           gen=lambda n: generators[stype](n, a, r)

        if(command=="sum"):
           print(sum_series(n, i, gen))
        if(command=="sequence"):
           sequence(n, i, gen)
