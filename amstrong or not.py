# N=given number
# s=sum
# n=total no.of digits in N
# t=temp
N=int(input("Enter the number:"))
s=0
n=len(str(N))
t=N
while t>0:
    d=t%10
    s=s+d**n
    t=t//10
if N == s:
    print(N, "is an Armstrong number")
else:
    print(N, "is not an Armstrong number")

