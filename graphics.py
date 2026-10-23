import matplotlib.pyplot as plt
import math
# Списки для первой функции x^2
x1 = []
y1 = []
x_int1 = []
y_int1 = []
# Списки для второй функции e^x
x2 = []
y2 = []
x_int2 = []
y_int2 = []
# Списки для третьей функции ln(x)
x3 = []
y3 = []
x_int3 = []
y_int3 = []
# Списки для четвертой функции x^3
x4 = []
y4 = []
x_int4 = []
y_int4 = []
# Считаем точки для x^2, e^x и x^3 в одном цикле
t = -3.0
while t <= 3.0:
    val_x = round(t, 2)
    # Первая функция
    x1.append(val_x)
    res1 = val_x ** 2
    y1.append(res1)
    # Вторая функция
    x2.append(val_x)
    res2 = math.exp(val_x)
    y2.append(res2)
    # Четвертая функция
    x4.append(val_x)
    res4 = val_x ** 3
    y4.append(res4)
    # Проверка на целое число
    if val_x == int(val_x):
        x_int1.append(val_x)
        y_int1.append(res1)
        
        x_int2.append(val_x)
        y_int2.append(res2)
        
        x_int4.append(val_x)
        y_int4.append(res4)
    t = t + 0.1
# Для логарифма делаем отдельный цикл т.к. x должен быть больше 0
t2 = 0.1
while t2 <= 5.0:
    val_x2 = round(t2, 2)
    x3.append(val_x2)
    res3 = math.log(val_x2)
    y3.append(res3)
    if val_x2 == int(val_x2):
        x_int3.append(val_x2)
        y_int3.append(res3)
    t2 = t2 + 0.1
# Рисуем все графики
plt.figure()
# Отрисовка линий
plt.plot(x1, y1, color="r", label="x^2")
plt.plot(x2, y2, color="b", label="e^x")
plt.plot(x3, y3, color="g", label="ln(x)")
plt.plot(x4, y4, color="m", label="x^3")
# Отрисовка точек
plt.scatter(x_int1, y_int1, color="r", marker="o")
plt.scatter(x_int2, y_int2, color="b", marker="x")
plt.scatter(x_int3, y_int3, color="g", marker="s")
plt.scatter(x_int4, y_int4, color="m", marker="^")
# Добавление сетки и подписей
plt.grid()
plt.legend()
plt.title("Graphics")
plt.show()
