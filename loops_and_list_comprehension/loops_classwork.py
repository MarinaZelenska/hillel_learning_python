"""
1. Для чого нам потрібні списки:
Уяивмо, що в нас є список і нам треба вивести кожен окремий елемент списку
"""

# my_list = [1, 2, 3, 4, 5]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
#
# for element in my_list:
#     print(element)


# names = ["Maryna", "Oleg", "Igor", "Yana"]
#
# for name in names:
#     if name == "Oleg":
#         continue
#     print(name)

# for number in range(4):
#     print(number, end=' ')

# for number in range(1, 4):
#     print(number, end=' ')
#
# for number in range(0, 101, 5):
#     print(number, end=' ')
# else:
#     print("That's over!")
#
# names = ["Maryna", "Oleg", "Igor", "Yana"]
# actions = ["work", "eat", "sleep", "enjoy"]
#
# for name in names:
#     for action in actions:
#         c = 0
#         print(name, ' ', action)


"""
while loop 
the classic explanation
break
continue
"""
# value = 1
# while value < 10:  # робота на True
#     print(value)
#     if value == 5:
#         break
#     value += 1


# while value < 10:  # робота на True - приклад бескінечного циклу
#     if value == 5:
#         continue
#     print(value)
#     value += 1


# while value < 10:  # робота на True
#     value += 1
#     if value == 5:
#         # break
#         continue
#
#     print(value)
# else:
#     print("Value", value) # this works if no break


# list_of_values = [1, 6, 7, 10]
# len_list = len(list_of_values)
# value = 1
#
# while len_list:
#     len_list -= 1
#     if list_of_values[len_list] == value:
#         print("Value was found")
#         break
# else:
#     print("Value was not found")

# Видалити дублікати зі списку


# lst = [1, 2, 2, 5, 6, 7, 6, 8, 8]
#
# for el in lst:
#     idx = lst.index(el)
#     if el in lst[idx+1: ]:
#         lst.remove(el)
# print(lst)



