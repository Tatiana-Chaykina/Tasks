a = float(input("Введите число для таблицы умножения: "))
for i in range(10):
    print(f"{i}", end="    ")
print("")
for j in range(10):
    b = j * a
    print(f"{b}", end=" ")