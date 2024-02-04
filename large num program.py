a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

if a > b and a > c:
    print(f"num a is a large num:{a}")
elif b > a and b > c:
    print(f"num b is a large num:{b}")
else:
    print(f"num c is a large num:{c}")
