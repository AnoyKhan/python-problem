def func(size, *toopings, **detils):
    print(f"Order a {size} pizza with the following toopings")
    for tooping in toopings:
        print(f"-{tooping}")
    print(f"\nDetails of the order are")
    for key, value in detils.items():
        print(f"-{key}: {value}")

func("Large", "mediam", "small", Delevery = True, tip = 5)

#----------------------------------------------------------------------------------------


def my_min(x, *y):
    y = min(y)
    if x<y:
        return x
    else:
        return y

print(my_min(8, 13, 34, 42, 120, 7))