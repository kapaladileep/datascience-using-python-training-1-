n = int(input(" enter the value of n:"));
if(n%2 == 0):
    print(n," is a  even number")
    if(n%5 == 0):
        print(n," is divisible by 5")
    else:
        print(n," is not divisible by 5")
else:
    print(n," is a odd number")
    if(n%5 == 0):
        print(n," is divisible by 5")
    else:
        print(n," is not divisible by 5")
for i in range(2,n):
    if(n%i==0):
        print(n," is not a prime number")
        break
else:
    print(n," is a prime number")
        
