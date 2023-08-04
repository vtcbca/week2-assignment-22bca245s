#Write a python script to enter any string, replace vowel with its position number.
For Example: input: Amit
             output:0m2t
str=input("Enter any string:")
v=['a','e','i','o','u','A','E','I','O','U']
u_str=""
for i in range (len(str)):
  if str[i]in v:
    u_str+=string(i)
  else:
    u_str+=str[i]
    print("\n\t Inputted string is :",str)
    print("\t After converting index number at vowels space the string is:",u_str)
