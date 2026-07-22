addition = lambda x,y: x + y
subtraction = lambda x,y: x - y
multiplication = lambda x,y: x * y
division = lambda x,y: x / y

x = int(input())
y = int(input())

print(f"addition: ",     addition(x,y))
print(f"subtraction: ",subtraction(x,y))
print(f"multiplication: ",multiplication(x,y))
print(f"division: ", division(x,y))
