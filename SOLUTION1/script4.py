#Write a script to enter any number and check it is armstrong number or not.
a=int(input("enter any number"))
sum=0
temp=a
while(a>0):
     b=a%10
     c=b*b*b
     a=a/10
     sum=sum=c
if(sum==temp):
      print("{} is armstrong".format(temp))
else:
      print("number is not armstrong:")
      
