a = float(input("Введите 1 число: "))
b = float(input("Введите 2 число: "))
if b % a == 0:
    print("Число", a, "является делителем числа", b)
else:
    print("Число", a, "не является делителем числа", b)