num=int(input("Enter no of items in list :"))
list=[int(input("enter the elements :")) for i in range (num)]
list=sorted(list)
print(list[-2])