from operator import index


def binary_search(arr, target):
    t=(len(arr))//2
    if len(arr)==0:
        return -1
    if len(arr)==1 and arr[0]!=target:
        return -1
    if arr[t]==target or len(arr)==1:
        return index(arr[t])-1
    if arr[t]>target:
        return binary_search(arr[:t],target)
    else:
        return binary_search(arr[t:], target)

# Пример использования
sorted_numbers = [1, 2, 3, 4, 5, 6, 7]
index_of_four = binary_search(sorted_numbers, 1)
print(index_of_four)  # Ожидаемый вывод: 3
index_of_eight = binary_search(sorted_numbers, 8)
print(index_of_eight)  # Ожидаемый вывод: -1
# Тест 1
assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3
# Тест 2
assert binary_search([1, 2, 3, 4, 5, 6, 7], 6) == 5
# Тест 3
assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == 0
# Тест 4
assert binary_search([1, 2, 3, 4, 5, 6, 7], 8) == -1
# Тест 5
assert binary_search([], 1) == -1  # Пустой массив
print("Все тесты пройдены!")