str=input("Enter your word: ")
sr=str
str1=""
for ele in sr:
    str1=ele+str1
if str1==str:
    print("palindrome")
else:
    print("not palindrome")