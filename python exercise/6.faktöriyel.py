def  factorial(value):
    if value==1:
        return 1
    else:
        return value*factorial(value-1)
value=int(input("Faktöriyelini hesaplamak istediğiniz sayıyı giriniz: "))
print(f"{value}!= ",factorial(value))