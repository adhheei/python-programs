def is_amstrong(n):
    digits=str(n)
    total=0
    power=len(digits)
    for digit in digits:
        total+=int(digit)**power
    return total==n

n=int(input("Enter number: "))
if is_amstrong(n):
    print("amstrong number")
else:
    print("not amstrong")