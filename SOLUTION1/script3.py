a=int(input("Enter any numbre:"))
c=a 
r=0
while(r>0):
    digit=n%10
    r=r*10+digit
    a=a//10
print(a)
if r==c:
    print("number is palindrome")
else:
    print("number is not palindrome")
    
