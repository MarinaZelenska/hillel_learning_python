"""
LECTURE: LIST COMPREHENSIONS IN PYTHON
=====================================

Ця лекція пояснює:
- Що таке list comprehension
- Навіщо він потрібен
- Як переписати звичайний цикл у comprehension
- Умови у comprehension
- Вкладені comprehension
"""


# ---------------------------------------------
# 1. ЩО ТАКЕ LIST COMPREHENSION
# ---------------------------------------------

# Це короткий синтаксис для створення списків.
# Замість того, щоб писати цикл і append(), можна зробити все в одному рядку.

# Приклад:
numbers = [1, 2, 3, 4, 5]

# Було:
result = []
for n in numbers:
    result.append(n * 2)

# Стало:
result_comp = [n * 2 for n in numbers]

print("Звичайний цикл:", result)
print("List comprehension:", result_comp)


# ---------------------------------------------
# 2. СТРУКТУРА COMPREHENSION
# ---------------------------------------------

# [ expression for item in iterable ]
# де:
# - expression → що саме ми додаємо у список
# - item → елемент під час перебору
# - iterable → список, рядок, діапазон, будь-яка колекція

squares = [x * x for x in range(1, 6)]
print("Квадрати:", squares)


# ---------------------------------------------
# 3. COMPREHENSION + УМОВА (IF)
# ---------------------------------------------

# Залишаємо тільки парні числа
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Парні числа:", evens)

# Додаємо слово до списку, якщо воно довше 4 букв
words = ["apple", "tea", "banana", "hi"]
long_words = [w for w in words if len(w) > 4]
print("Довгі слова:", long_words)


# ---------------------------------------------
# 4. IF–ELSE У COMPREHENSION
# ---------------------------------------------

# Структура:
# [ expression_if_true if condition else expression_if_false for item in iterable ]

labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print("even/odd:", labels)


# ---------------------------------------------
# 6. ВКЛАДЕНІ LIST COMPREHENSION
# ---------------------------------------------

# Створити всі комбінації чисел
pairs = [(x, y) for x in range(1, 3) for y in range(10, 13)]
print("Пари:", pairs)


# ---------------------------------------------
# 7. ПРАКТИЧНІ ПРИКЛАДИ
# ---------------------------------------------

# 1. Піднести кожне число до куба
cubes = [x ** 3 for x in range(1, 6)]
print("Куби:", cubes)

# 2. Витягнути перші букви зі слів
cities = ["London", "Paris", "Berlin", "Kyiv"]
initials = [city[0] for city in cities]
print("Перші букви:", initials)

# 3. Замінити гласні на "*"
vowels = "aeiou"
masked = ["*" if char in vowels else char for char in "banana"]
print("Маска:", masked)

# 4. Утворити список тільки позитивних чисел
nums = [-3, 0, 2, -1, 5]
positives = [n for n in nums if n > 0]
print("Позитивні:", positives)


