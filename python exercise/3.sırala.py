#selection sort
def selection_sort(liste):
    for i in range(len(liste)-1):
        eleman=liste[i]
        index=i
        for j in range(i+1,len(liste)):
            if eleman > liste[j]:
                eleman=liste[j]
                index=j
        bekle_1=liste[i]
        liste[i]=liste[index]
        liste[index]=bekle_1
    print(liste)

#bubble sort
def bubble_sort(liste):
    for k in range(len(liste)):
        for n in range(len(liste)-k-1):
            if (liste[n]>liste[n+1]):
                liste[n], liste[n + 1] = liste[n + 1],liste[n]
    print(liste)

#insertion sort
def insertion_sort(liste):
     for k in range(1,len(liste)):
      key=liste[k]
      j=k-1
      while j>=0 and key<liste[j]:
        liste[j + 1] = list[j]
        j = j - 1
        liste[j + 1] = key

liste=[9,40,17,68,96,1]
print(selection_sort(liste))
print(bubble_sort(liste))
print(insertion_sort(liste))