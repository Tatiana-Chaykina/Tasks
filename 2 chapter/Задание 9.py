a = float(input("Введите первое значение: "))
b = float(input("Введите второе значение: "))
c = float(input("Введите третье значение: "))
if a > b and a > c:
    m = a
    print("Наибольшее значение:", m)
if b > a and b > c:
    m = b
    print("Наибольшее значение:", m)
if c > a and c > b:
    m = c
    print("Наиболшее знаяение:", c)
if a == b == c:
    print("Наибольшего знаяения нет, все равны")