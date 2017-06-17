import sys

#Fibonacci series 

def fib(x):                        #defining function 
    if x == 0 or x == 1:
          return 1                  
    else:
        return fib(x-1)+fib(x-2)                #recursive part