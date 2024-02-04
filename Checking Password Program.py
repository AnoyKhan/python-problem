from getpass import getpass
Type_password = str(input("Type password: "))
ReType_password = str(input("ReType Password: "))
if Type_password == ReType_password:
    print("welcome, please come in ")
else:
    print("password not matched")


