import matplotlib.pyplot as plt
length=[176,180,187,182,175,190,184,177,180,179]
weight=[66,83,80,75,73,70,90,84,83,79]
name=["zafer","emre","ahmet","ayşe","fatma","hasan","mehmet","furkan","hakan","metin"]
# for i in range(3):
#     name.append(input("name: "))
#     length.append(input("lenght(cm): "))
#     weight.append(input("weight(kg): "))
plt.figure(figsize=(12,6))
plt.plot(name,length,"o--g")
plt.plot(name,weight,"o--r")
plt.title("Name-Length-Weight") 
plt.xlabel("Name")
plt.ylabel("Weight-Length")
plt.grid(True,color='black')
plt.legend(["Length","Weight"])
plt.show()