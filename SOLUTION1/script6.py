#Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
 str=input("Enter a string: ")   
 start=int(input("Enter the starting index:"))
 end=int(input("Enter the end index:"))
 substring=str[start:end]
 print("\n Substring which starts from",start,"index no. and ends at",end,"index no. is : ", substring)
