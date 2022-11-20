import numpy as np
def sarrus_method(x):
    det=(x[0][0]*x[1][1] + x[1][0]*x[2][1] + x[2][0]*x[0][1])-(x[1][0]*x[0][1] + x[2][0]*x[1][1] + x[0][0]*x[2][1])
    return abs(det)/2
controls_x=[]
controls_y=[]
for i in range(3):
    controls_x.append(int(input(f"Lütfen {i+1}. x noktasını giriniz: ")))
for j in range(3):
    controls_y.append(int(input(f"Lütfen {j+1}. y noktasını giriniz: ")))
print("Oluşan üçgeninizin noktaları:")
for k in range(3):
    print(f"{(controls_x[k],controls_y[k])}")
control_x=input("Lütfen x noktanızı giriniz:")
control_y=input("Lütfen y noktanızı giriniz:")
s=0
for i in range(3):
    main_triangle=np.array([[controls_x[0],controls_y[0]],
                            [controls_x[1],controls_y[1]],
                            [controls_x[2],controls_y[2]]])
    if i==0:
        total_area=sarrus_method(main_triangle)
    main_triangle[i]=[control_x,control_y]
    new_area=sarrus_method(main_triangle)
    s=s+new_area
if s == total_area:
    print(f"{(control_x,control_y)} noktaları üçgenin içindedir")
else:
    print(f"{(control_x,control_y)} noktaları üçgenin dışındadır")