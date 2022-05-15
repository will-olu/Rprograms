import math


#def fibonacci(n, k):
   # value= (((1.618034)**n) - ((1-1.618034)**n))/math.sqrt(5)
   # value = value * k
   # return (value)



#fibonacci(5, 3)
#print (fibonacci(5, 3))


# Program to display the Fibonacci sequence up to n-th term

###def fib(n, k):
    #previous1, previous2 = 1, 1
    ##for i in range(2, n):
        #previous1, previous2 = previous2, previous1 * k + previous2
    #return previous2

def rabbits(n, k):
    prev1 = 1
    prev2 = 1
    for i in range(2, n):
        current = prev1 + k * prev2
        prev2 = prev1
        prev1 = current
    return current
rabbits(28, 3)
print(rabbits(28,3))



#def FibRecursion(n):  
  # if n <= 1:  
       #return n  
   #else:  
       #return(FibRecursion(n-1) + FibRecursion(n-2))  
#nterms = int(input("Enter the terms? "))  # take input from the user

  
#if nterms <= 0:  # check if the number is valid 
   #print("Please enter a positive integer")  
#else:  
   #print("Fibonacci sequence:")  
   #for i in range(nterms):  
       #print(FibRecursion(i))
