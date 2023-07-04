# s=given string
# r=reverse of the string
s=str(input("enter the string:"))
r=str(s)[::-1]
if s==r:
    print(s,"is a palindrome string")
else:
    print(s,"is not a palindrome string")