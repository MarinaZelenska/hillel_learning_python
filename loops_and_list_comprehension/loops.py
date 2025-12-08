"""
LECTURE: Loops in Python
========================

This file contains:
- For loop
- While loop
- range()
- enumerate()
- random module
- Practice tasks
"""

# ---------------------------------------------
# 1. ЦИКЛ FOR
# ---------------------------------------------

print("\n=== 1. ЦИКЛ FOR ===")

# Цикл for використовується для перебору послідовностей
numbers = [10, 20, 30]

print("Приклад простого for:")
for num in numbers:
    print("Число:", num)

# ---------------------------------------------
# 2. ФУНКЦІЯ range()
# ---------------------------------------------

print("\n=== 2. ФУНКЦІЯ range() ===")

print("range(5) → від 0 до 4:")
for i in range(5):
    print(i)

print("\nrange(1, 6) → 1...5:")
for i in range(1, 6):
    print(i)

print("\nrange(0, 10, 2) → крок 2:")
for i in range(0, 10, 2):
    print(i)

# ---------------------------------------------
# 3. ФУНКЦІЯ enumerate()
# ---------------------------------------------

print("\n=== 3. ФУНКЦІЯ enumerate() ===")

fruits = ["apple", "banana", "orange"]

print("Перебір зі збереженням індекса:")
for index, fruit in enumerate(fruits):
    print(index, "→", fruit)

print("\nstart=1:")
for index, fruit in enumerate(fruits, start=1):
    print(index, "→", fruit)

# ---------------------------------------------
# 4. ЦИКЛ WHILE
# ---------------------------------------------

print("\n=== 4. ЦИКЛ WHILE ===")

print("Відлік від 5 до 1:")
i = 5
while i > 0:
    print(i)
    i -= 1

# while з умовою "поки користувач не введе 0"
print("\nВведи числа (0 щоб зупинити):")
# >>> Uncomment to test
# num = int(input("Enter number: "))
# while num != 0:
#     print("Ви ввели:", num)
#     num = int(input("Enter number: "))


# ---------------------------------------------
# 5. МОДУЛЬ random
# ---------------------------------------------

print("\n=== 5. МОДУЛЬ random ===")
import random

print("Випадкове число 1–10:", random.randint(1, 10))

numbers = [1, 2, 3, 4, 5]
print("Випадковий елемент з списку:", random.choice(numbers))

print("Перемішування списку shuffle():")
random.shuffle(numbers)
print(numbers)

print("Випадкове число з плаваючою точкою 0–1:", random.random())

# ---------------------------------------------
# 6. ПРАКТИЧНІ ЗАДАЧІ
# ---------------------------------------------

print("\n=== 6. ПРАКТИЧНІ ЗАДАЧІ ===")

print("\n1. Сума чисел від 1 до N")


def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print("sum_to_n(10) =", sum_to_n(10))

print("\n2. Кількість голосних у слові")


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


print("count_vowels('Banana') =", count_vowels("Banana"))

print("\n3. Генерація випадкового списку та перебір з enumerate()")
random_list = [random.randint(1, 100) for _ in range(5)]
print("Випадковий список:", random_list)

for index, value in enumerate(random_list):
    print(f"Елемент {index}: {value}")

print("\n4. Поки випадкове число не буде 7")
attempt = 1
while True:
    x = random.randint(1, 10)
    print(f"Спроба {attempt}: випало {x}")
    if x == 7:
        print("Випало число 7 — стоп!")
        break
    attempt += 1
