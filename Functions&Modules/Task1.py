
def fact(num):
    total = 1
    for i in range(1,num+1):
        total = total * i
    return total

a = int(input("Enter the number to calculte its factorial:  "))

result = fact(a)
print(f"The factorial of {a} is {result}")