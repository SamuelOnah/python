print("=== SIMPLE CALCULATOR ===")



num1  = float(input("Enter First number: ")) # float() handler decimals
num2 = float(input("Enter second number: "))
num1  = int(input("Enter First number: ")) # Note the differnce this works without float
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
divisions = num1 / num2


print("\n---RESULT---")
print(num1, "+", num2, "=", sum_result)
print(num1, "-",  num2, "=", difference)
print(num1, "*", num2, "=", product)
print(num1,"/", num2, "=", divisions)

