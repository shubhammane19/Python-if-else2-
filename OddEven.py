num1 = int(input("Enter number1: "))
num2 = int(input("Enter number2: "))
ans = num1+num2

if((num1+num2)% 2 == 0):
    print(ans, "is even", end =" ")
else:
    print(ans, "is odd", end = " ")