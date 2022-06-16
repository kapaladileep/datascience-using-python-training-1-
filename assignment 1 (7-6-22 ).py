a = int(input("enter the annual income:"));
b = int(input("enter the value of HRA:"));
c = int(input("enter the value of other decductions:"));
if(c>80000):
    print("deductions cant be more than the 80000")
else:
    x = a - b - c
    Y = x - 300000
    if(Y <= 300000):
        print("no tax")
    elif(Y > 300000 and Y <= 600000):
        tax = 0.1*Y
        print("tax to be paid=", tax)
    elif(Y > 600000 and Y <= 1000000):
        tax1 = 0.15*Y
        print("tax to be paid=", tax1)
    else:
        tax2 = 0.2*Y
        print("tax to be paid=", tax2)
        




