"""
@author 
zafer tunçer
mail=zafertncr66@gmail.com
"""
class Student:
    def __init__(self):
        self.fonk_run=True
        print("Öğrenci Otomasyon Sistemine Hoşgeldiniz.")
        secim=int(input("Lütfen yapmak istediğiniz işlemi seçiniz:1-)Öğrenci Kayıt\n2-)Öğrenci Bilgi Sorgulama\n3-)Öğrenci Bilgisi Silme\n4-)Çıkış\nSeçim= "))
        if secim==1:
            self.kayıt()
        if secim==2:
            self.Bilgi_Sorgulama()
        if secim==3:
            self.silme()
        if secim==4:
            self.çıkış()
    def kayıt(self):
        self.isim=input("isim:")
        self.soyisim=input("soyisim:")
        self.yaş=int(input("yaş:"))
        self.sınıf=int(input("sınıf:"))
        self.cinsiyet=input("cinsiyet:")
        with open("ogrenci.txt","r+",encoding="utf-8") as f:
            no=len(f.readlines())+1
            f.write(f"{no}-){self.isim} {self.soyisim}=> yaşı:{self.yaş} sınıfı:{self.sınıf} cinsiyet:{self.cinsiyet}\n")
    def Bilgi_Sorgulama(self):
        hangi_ogrenci=input("Kontol etmek istediğiniz öğrencinin numarası giriniz: ")
        with open("ogrenci.txt","r",encoding="utf-8") as f:
            oku=f.readlines()
            for a in range(len(oku)):
                if oku[a][0:1] == hangi_ogrenci:
                    print(oku[a])
                else:
                    print(f"{hangi_ogrenci} numaralı öğrenci bulunmamaktadır.")
    def silme(self):
        sil=int(input("Silmek istediğiniz öğrencinin numarası giriniz: "))
        with open("ogrenci.txt","r",encoding="utf-8") as f:
            oku=f.readlines()
            print(oku)
            oku[sil-1]="\n"
            print(oku)
        with open("ogrenci.txt","w",encoding="utf-8") as f:
            print(oku)
            for i in oku:
                f.write(i)
    def çıkış(self):
        pass
fonk_run=True
while fonk_run:
    Student()