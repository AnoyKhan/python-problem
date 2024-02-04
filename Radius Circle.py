import math

def calculate_area(radius):
    my_area = math.pi*radius**2
    return my_area
radius = calculate_area(int(input("please input the radius:")))
print("The area of circle is:", radius)



def largest():
    number1 = int(input("Enter the value of 1st number :"))
    number2 = int(input("Enter the value of 2nd number :"))
    if (number1 > number2):
        print("Largest is number1 & it is =",number1)
    else:
        print("Largest is number2 & it is =",number2)

largest()
