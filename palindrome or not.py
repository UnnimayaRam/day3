# n=given number
# r=reverse of the number
n=int(input("enter the number:"))
r=str(n)[::-1]
if n==r:
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")

