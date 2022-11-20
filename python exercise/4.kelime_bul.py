kontrol_cümlesi=input("lütfen kontrol edilecek cümleyi giriniz: ")
liste=kontrol_cümlesi.lower()#büyük küçük harf duyarlılığından kaynaklı hepsini küçültülmüş şekilde kontrol ederiz
print(kontrol_cümlesi)
liste=liste.split()
print(liste)
aranan_kelime=input("Lütfen aranan keliyemi giriniz: ")
aranan_kelime=aranan_kelime.lower()
for i in range(len(liste)):
    if liste[i]==aranan_kelime:
        print("aranan "+liste[i]+" kelimesi cümlede bulunmaktadır")