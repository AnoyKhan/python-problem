def string_reverse(str1):
    rstr1 =(str(input("Enter the value")))
    index = len(str1)
    while index > 0:
        rstr1+=str1[index - 1]
        index = index - 1
        return rstr1
    print(string_reverse(rstr1))

