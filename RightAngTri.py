angle1  = int(input("Enter angle1: "))
angle2  = int(input("Enter angle2: "))
angle3  = int(input("Enter angle3: "))

if(angle1 == 90 or angle1 == 60 or angle1 == 30) and (angle2 == 60 or angle2 == 30 or angle2 == 90) and (angle3 == 30 or angle3 == 90 or angle3 == 60) and (angle3!=angle2!=angle1):
    print("It is a right-angle triangle", end = " ")
else:
    print("It is not a right-angle triangle", end = " ")