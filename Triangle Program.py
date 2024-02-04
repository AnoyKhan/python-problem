import math

def Tringale():
    a = str(input("Enter the value of a:"))
    b = str(input("Enter the value of b:"))
    c = str(input("Enter the value of c:"))

    if (a+b)>c and (b+c)<a and (c + a)<b:
        s = (a + b+ c)/ 2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c)*(s-b)*(s-c))
        print("Area of the triangle is:", area)

    else:
        print("The triangle is not possible")

Tringale()


def calculate_area(radius):
    myarea = math.pi*radius**2
    return myarea
radius = calculate_area(int(input("please enter the redius:")))
print(radius)

