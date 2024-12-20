from operator import index


def ternary_search(arr, target):
    t1 = (len(arr)) // 3
    t2=len(arr)-t1
    if len(arr) == 0:
        return -1
    if len(arr) == 2 and (arr[1] != target and arr[0] != target):
        return -1
    if arr[t1] == target or arr[t2]==target or len(arr) == 1:
        return index(arr[t1]) - 1
    if arr[t1]<target and arr[t2]>target:
        arr=arr[t1:]
        arr=arr[:t2]
        return ternary_search(arr,target)
    if arr[t1] < target:
        return ternary_search(arr[t1:], target)
    if arr[t2] > target:
        return ternary_search(arr[:t2], target)

# Пример использования
sorted_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index_of_five = ternary_search(sorted_numbers, 5)
print(index_of_five)  # Ожидаемый вывод: 4

index_of_ten = ternary_search(sorted_numbers, 10)
print(index_of_ten)  # Ожидаемый вывод: -1
# Тест 1
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 4
# Тест 2
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 2
# Тест 3
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1) == 0
# Тест 4
assert ternary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10) == -1
# Тест 5
assert ternary_search([], 1) == -1  # Пустой массив
print("Все тесты пройдены!")