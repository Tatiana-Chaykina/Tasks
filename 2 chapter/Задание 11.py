elements = []
num_elements = int(input("Введите сколько элементов в массиве хотите: "))
for i in range(num_elements):
    element = input("Введите элемент:")
    elements.append(element)
    min_element = min(elements)
print("Минимальное значение элемента в массиве:", min_element)