import random

# ---------------------------------------------------------
# 1. Fizz для чисел, кратних 3
# ---------------------------------------------------------
my_list = [1, 2, 3, 4, 5]
for idx, el in enumerate(my_list):
    if el % 3 == 0:
        my_list[idx] = 'Fizz'

print(my_list)




# ---------------------------------------------------------
# 2. Сума всіх непарних чисел від 1 до 100
# ---------------------------------------------------------
num = 0
for el in range(1, 11):
    if el % 2 != 0:
        num += el

print(num)




# ---------------------------------------------------------
# 3. Порахувати кількість цифр у числі
# ---------------------------------------------------------
num = int(input("Enter your number: "))
quantity = 0
while num > 0:
    quantity += 1
    num //= 10
print(quantity)


# ---------------------------------------------------------
# 4. Таблиця множення для числа N
# ---------------------------------------------------------
selected_number = int(input("Enter your number: "))

for el in range(1, 11):
    result = selected_number * el
    print(selected_number, " * ", el, " = ", result)



# ---------------------------------------------------------
# 5. Гра: вгадати випадкове число від 1 до 10
# ---------------------------------------------------------



num_guess = int(input("Enter your number: "))
random_num = random.randint(0, 10)
tries = 10

while tries > 0:
    if num_guess == random_num:
        print("You are guess")
        break
    tries -= 1
    num_guess = int(input("Try again. Enter your number: "))
else:
    print("Unfortunately, you are not a guess")










