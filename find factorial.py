# n=given numbers
# f=factorial
# there is no factorial in negative number
n=int(input("Enter a number:"))
f=1
if n>=1:  #check the number is positive
    for i in range (1, n+1):
        f= f*i
print ("Factorial of the given number is:",f)
