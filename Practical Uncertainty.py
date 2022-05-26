from math import sqrt

uncertainty_value1 = float(input("Enter the first uncertainty: "))
value1 = float(input("Enter the first value: "))

uncertainty_value2 = float(input("Enter the second uncertainty: "))
value2 = float(input("Enter the second value: "))

answer = float(input("Enter the final result: "))

value1_squared = (uncertainty_value1 / value1) ** 2

value2_squared = (uncertainty_value2 / value2) ** 2

return_value = answer * (sqrt(value1_squared + value2_squared))

print("\n\nThe uncertainty is ", return_value)
