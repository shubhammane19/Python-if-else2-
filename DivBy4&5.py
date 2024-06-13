num = int(input("Enter number: "))

if(num % 4 == 0) and (num % 5 == 0):
    print("{} is divisible by 4 and 5".format(num), end = " ")
else:
    print("{} is not divisble by 4 and 5".format(num), end = " ")