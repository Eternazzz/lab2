height=float(input(("Введите рост: ")))
weight=float(input(("Введите вес: ")))
count=float(input(("Введите кол-во шагов: ")))
time=float(input(("Введите время активности: ")))
stride_l=(height/4)+0.37
S=stride_l*count
V=S/(time*60)
calories=0.035*weight+(V**2)/height*0.029*weight
S=round(S,3)
calories=round(calories,3)
print(f'Пройденная дистанция:{S} Кол-во соженных калорий в минуту:{calories}')
km=S/1000
print(f'Кол-во пройденных км:{km}')
if km<2:
    print("Вы прошли меньше двух километров, необходимо работать усерднее!")
elif km<4:
    print("Вы прошли больше двух километров,неплохо, но можно лучше!")
else:
    print("Прекрасно! Вы прошли больше 4 километров")
