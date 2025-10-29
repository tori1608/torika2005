def get_positive_integer(prompt):
    while True:
        value = input(prompt)
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print("Ошибка! Введите целое положительное число.")

def check_pythagorean_theorem(leg1, leg2, hypotenuse):
    return leg1 * leg1 + leg2 * leg2 == hypotenuse * hypotenuse

# Ввод данных
a = get_positive_integer("Введите длину первого отрезка: ")
b = get_positive_integer("Введите длину второго отрезка: ") 
c = get_positive_integer("Введите длину третьего отрезка: ")

# Определяем гипотенузу (наибольшую сторону)
if a > b and a > c:
    hyp = a
    leg1, leg2 = b, c
elif b > a and b > c:
    hyp = b
    leg1, leg2 = a, c
else:
    hyp = c
    leg1, leg2 = a, b

print(f"Катеты: {leg1} и {leg2}, гипотенуза: {hyp}")

if check_pythagorean_theorem(leg1, leg2, hyp):
    print("Результат: треугольник является прямоугольным")
else:
    print("Результат: треугольник не является прямоугольным")

