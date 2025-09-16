str=input("enter a string :")
sr=str
str1=""
for ele in str:
    str1=ele+str1
if str1==sr:
    print("Its a palindrome")
else:
    print("Its not a palindrome")