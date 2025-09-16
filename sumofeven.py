def sum_of_even(numbers):
    return sum(num for num in numbers if num%2==0)

n=int(input("enter how many numbers :"))
numbers=[]
for i in range(n):
    num=int(input(f"enter the number {i+1}: "))
    numbers.append(num)
print("Your list:",numbers)
print("Sum of even numbers:",sum_of_even(numbers))