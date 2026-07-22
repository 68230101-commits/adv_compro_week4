from utilities.calculator import add, subtract, multiply, divide
from utilities.string_operations import reverse_string, capitalize_string, lowercase_string, uppercase_string

a = 10
b = 5

print("Using calculator.py:")
print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))

sample_string = "hello World"

print("\nUsing string_operations.py:")
print("OG:", sample_string)
print("Rev:", reverse_string(sample_string))
print("Cap:", capitalize_string(sample_string))
print("Low:", lowercase_string(sample_string))
print("Up:", uppercase_string(sample_string))
