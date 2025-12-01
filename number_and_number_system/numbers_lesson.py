# ============================================
# 1. Numeric data types in Python
# ============================================

# int – integer numbers
a = 10
b = -5

# float – decimal numbers
c = 3.14
d = -0.5


print("int example:", a)
print("float example:", c)


# type() shows the data type of a variable
print("Type of a:", type(a))
print("Type of c:", type(c))

# ============================================
# 2. Memory and id()
# ============================================

# id() returns a unique identifier (memory address reference)
x = 100
y = 100
z2 = 200

print("ID of x:", id(x))
print("ID of y:", id(y))  # x and y may share memory because small integers are cached
print("ID of z2:", id(z2))

# Reassigning changes the memory location
x = x + 1
print("New value of x:", x)
print("New ID of x:", id(x))

# ============================================
# 3. Mathematical operators
# ============================================

print("Addition:", 5 + 3)
print("Subtraction:", 7 - 2)
print("Multiplication:", 4 * 6)
print("Division:", 8 / 3)
print("Floor division:", 8 // 3)
print("Modulo (remainder):", 8 % 3)
print("Exponentiation:", 2 ** 5)

# ============================================
# 4. Using the math module
# ============================================

import math

print("math.pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("2 to the power of 3 using math.pow:", math.pow(2, 3))

# ============================================
# 5. input() function
# ============================================

# input() always returns a string, so we convert it to int or float
name = input("Enter your name: ")
print("Hello,", name)

age = int(input("Enter your age: "))
print("Next year you will be:", age + 1)

# ============================================
# 6. Mini tasks for practice
# ============================================

# Task 1: User enters two numbers, print their sum
x = float(input("Enter number x: "))
y = float(input("Enter number y: "))
print("Sum:", x + y)

# Task 2: Calculate the perimeter of a rectangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
perimeter = 2 * (a + b)
print("Perimeter =", perimeter)

# Task 3: Area of a circle (πr²)
r = float(input("Enter circle radius: "))
area = math.pi * r ** 2
print("Area of the circle:", area)

# Task 4: Show memory id of a variable entered by the user
num = int(input("Enter any integer: "))
print("You entered:", num)
print("Type:", type(num))
print("Memory ID:", id(num))
