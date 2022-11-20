deger=int(input("lütfen bölenlerini bulmak istediğiniz sayıyı giriniz: "))
bölenler=[]
for i in range(1,deger+1):
    if deger%i==0:
        bölenler.append(i)
print(bölenler)