def calc(x):
#variable jei koita, fund er moddhe same sei koita variable nite hobe
    perameter = x * 4
    area = x * x
    return perameter, area
    
side = int(input("please enter the number: "))
p, a = calc(side) # variable duitaa/ value just ekta- func call kora hoise
#p mean first variable and a mean second variable in func
print(f"Perimeter: {p}\nArea: {a}")