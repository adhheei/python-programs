from math import factorial

num=int(input("Enter a number: "))
if num<0:
    print("Negative number have no factorial")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range (1,num+1):
        print(f"factorial of {i} is {factorial(i)}")

