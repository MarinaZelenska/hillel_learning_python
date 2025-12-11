# TASK 1 Порахувати кількість голосних у строці
# import random
# import string
#
# length = 30
# characters = string.ascii_lowercase + string.ascii_uppercase
# result = ""
# vowels = "aeiou"
# count = 0
# for _ in range(length+1):
#     result += random.choice(characters)
#
# for letter in result:
#     if letter.lower() in vowels:
#         count += 1
#
# print(f'The {result} string has {count} vowels.')


# TASK 2 Перевірити, чи є рядок паліндромом

# palindrome_str  = "A roza upala na lapu Azora"
# not_palindrome_str = "Hello world"
#
# result = palindrome_str.lower().replace(" ", "")[::-1] == palindrome_str.lower().replace(" ", "")
# print(f"The string {palindrome_str} is palindrome = {result}")


# TASK 3 Знайти перший унікальний символ у рядку
#
# my_string = "LSEN?GvSnvbzksdnf"
#
# for letter in my_string:
#     result = my_string.count(letter)
#     if result > 1:
#         print(f"The first not unique symbol {letter}")
#         break

# Task 4 Порахувати кількість слів у реченні
# string_with_spaces = " learning  Python with Hillel Python basic course code ".split()
# print(len(string_with_spaces))

# Task 5 Замінити цифри в рядку на символ *
# phone = "My phone is 3801234567"
#
# for letter in phone:
#     if letter.isdigit():
#         phone = phone.replace(letter, "*")
#
# print(phone)


# Task 6 Видалити повторювані символи, залишивши тільки першу появу

# my_str = "banana"
# new_str = ""
#
# for letter in my_str:
#     if letter not in new_str:
#         new_str += letter
#
# print(new_str)

# Task 7 Визначити найчастіший символ у рядку


# my_str = "banana"
# counter = 0
# symbol = ''
#
# for element in my_str:
#     count_element = my_str.count(element)
#     if count_element > counter:
#         counter, symbol = count_element, element
# print(f'The most popular symbol is {symbol} = {counter} repetitions')

# Task 8 Зробити першу букву кожного слова великою
# my_str = "banana apple test"
# print(my_str.title())
# print(my_str.capitalize())
# print(my_str.swapcase())

# Task 9 Порахувати суму всіх чисел, які зустрічаються в рядку
# phone = "My phone is 3801234567"
# result = 0
#
# for el in phone:
#     if el.isdigit():
#         result += int(el)
# print(result)


# Task 10 Скоротити рядок: якщо довжина > 10, показати перші 5 + "..." + останні 3

# test = "internationalization"
# len_str = len(test)
# new_str = ''
#
# if len_str > 10:
#     new_str = test[:6] + "..." + test[-3:]
# print(new_str)



"""
намалювати
*****
*****
*****
*****
*****
"""


# for hight in range(1, 6):
#     for width in range(1, 6):
#         print('*', end='')
#     print()


"""
Намалювати
**********
*        *
*        *
*        *
**********
"""
for hight in range(1, 11):
    for width in range(1, 11):
        if hight == 1 or hight == 10 or width == 1 or width == 10:
            print("*", end="")
        else:
            print(" ", end="")
    print()

