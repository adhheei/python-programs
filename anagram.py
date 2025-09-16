def is_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    return sorted(str1)==sorted(str2)

str1=input("Enter first string: ")
str2=input("Enter second string: ")

if is_anagram(str1,str2):
    print("They are anagrams")
else:
    print("They are not anagrams")