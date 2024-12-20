a = float(input("Введите число для таблицы умножения: "))
for i in range(10):
    b = i * a
    print(f"{a}*{i}={b}", end=" ")