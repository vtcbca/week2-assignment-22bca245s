#Write a python script to enter any number and print the sum of its digit.
a=int(input("Enter any number:"))
sum=0
while(a>0):
    b=a%10
    sum=sum+b
    a=a/10
print("sum of digit of no {}is{}".format(a,sum))  
