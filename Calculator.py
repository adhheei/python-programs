class Calculater:
    def add (self,a,b):
        return a+b

    def sub (self,a,b):
        return a-b

    def mul (self,a,b):
        return a*b

    def div (self,a,b):
        if b!=0:
            return a/b
        else:
            return "error!"



cal=Calculater ()

print("choose operation: 1.Add 2.Sub 3.Mul 4.Divide")
choice=int(input("Enter choice (1/2/3/4)"))

a=float(input("Enter first number: "))
b=float(input("Enter Second number: "))

if choice==1:
    print(cal.add(a,b))

elif choice==2:
    print(cal.sub(a,b))

elif choice==3:
    print(cal.mul(a,b))

elif choice==4:
    print(cal.div(a,b))

else:
    print("error")