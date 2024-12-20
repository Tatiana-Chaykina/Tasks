import random  # Используем для выбора pivot случайным образом

def quick_sort_deck(deck):
    if len(deck) <= 1:
        return deck
    a = random.choice(deck)
    left = [x for x in deck if x < a]
    middle = [x for x in deck if x == a]
    right = [x for x in deck if x > a]
    return quick_sort_deck(left) + middle + quick_sort_deck(right)

# Пример использования
deck = [4, 2, 7, 1, 3, 5]
sorted_deck = quick_sort_deck(deck)
print(sorted_deck)  # Ожидаемый вывод: [1, 2, 3, 4, 5, 7]

# Тест 1
assert quick_sort_deck([4, 2, 7, 1, 3, 5]) == [1, 2, 3, 4, 5, 7]
# Тест 2
assert quick_sort_deck([10, 5, 3, 8]) == [3, 5, 8, 10]
# Тест 3
assert quick_sort_deck([1]) == [1]
# Тест 4
assert quick_sort_deck([3, 2]) == [2, 3]
# Тест 5
assert quick_sort_deck([7, 3, 3, 4, 1, 2, 5]) == [1, 2, 3, 3, 4, 5, 7]
print("OK!")