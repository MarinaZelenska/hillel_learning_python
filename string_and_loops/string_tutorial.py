# ================================================================
#                 ЛЕКЦІЯ: STRING У PYTHON
#               Повна теорія + приклади + задачі
# ================================================================
from tempfile import TemporaryDirectory

# ------------------------------------------------
# 1. ЩО ТАКЕ STRING
# ------------------------------------------------
# Рядок — це послідовність символів.
# Тип: str
# Важливо: строки IMMUTABLE → не можна змінити символ за індексом.
# ------------------------------------------------

s = "Hello"
print(type(s))  # <class 'str'>


# ------------------------------------------------
# 2. СТВОРЕННЯ РЯДКІВ
# ------------------------------------------------

a = 'Hello'
b = "World"
c = """Multiline
string"""

raw = r"C:\new_folder\test"  # raw-string

print(a, b, c, raw)


# ------------------------------------------------
# 3. ІНДЕКСАЦІЯ ТА СЛАЙСИ
# ------------------------------------------------

s = "Python"

print(s[0])     # P
print(s[-1])    # n
print(s[1:4])   # yth
print(s[::-1])  # nohtyP (реверс)


# ------------------------------------------------
# 4. ОСНОВНІ ОПЕРАЦІЇ
# ------------------------------------------------

print("Hello " + "World")   # конкатенація
print("ha" * 3)             # повторення
print(len("Python"))        # довжина
print("a" in "banana")      # True


# ------------------------------------------------
# 5. БАЗОВІ МЕТОДИ STRING
# ------------------------------------------------

text = "  hello world  "

print(text.lower())       # hello world
print(text.upper())       # HELLO WORLD
print(text.strip())       # hello world
print(text.title())       # Hello World
print(text.startswith("  h"))  # True

print("banana".find("na"))   # 2
print("banana".count("a"))   # 3


# ================================================================
# 6. Додаткові методи
# ================================================================

# ----------------------------
# replace()
# ----------------------------
print("Hello World".replace("World", "Python"))

print("aaa".replace("a", "b", 2))  # bba


# ----------------------------
# split()
# ----------------------------
print("one two three".split())           # ['one', 'two', 'three']
print("2024-12-01".split("-"))           # ['2024', '12', '01']


# ----------------------------
# join()
# ----------------------------
words = ["Python", "is", "awesome"]
print(" ".join(words))                   # Python is awesome


# ----------------------------
# partition()
# ----------------------------
email = "admin@test.com"
print(email.partition("@"))
# ('admin', '@', 'test.com')


# ----------------------------
# encode()
# ----------------------------
word = "Привіт"
encoded = word.encode("utf-8")
decoded = encoded.decode("utf-8")

print(encoded)
print(decoded)


# ================================================================
# 7. ФОРМАТУВАННЯ РЯДКІВ
# ================================================================

name = "Marina"
age = 32

# f-string
print(f"My name is {name} and I am {age} years old.")

# format()
print("User {} is {} years old".format(name, age))

# %
print("%s is %d years old" % (name, age))


# ================================================================
# 8. ДОДАТКОВІ ПРИКЛАДИ МАНІПУЛЯЦІЙ
# ================================================================

text = "Hello world from Python"

# Реверс порядку слів
rev_words = " ".join(text.split()[::-1])
print(rev_words)

# Видалити символ
print("banana".replace("a", ""))    # bnn

# Нормалізація вводу
name = "   marina zelenska  ".strip().title()
print(name)



# ================================================================
# 11.ЗАДАЧІ (з відповідями)
# ================================================================

# 1. Перший і останній символ
s = "Python"
print(s[0], s[-1])

# 2. Перевірити чи починається з Py
print(s.startswith("Py"))

# 3. Замінити пробіли на _
txt = "hello world"
print(txt.replace(" ", "_"))

# 4. Розділити email
print("email@test.com".partition("@"))

# 5. Зібрати речення
print(" ".join(["Python", "is", "cool"]))


# 6. Реверс букв кожного слова

sentence = "Hello world"
rev = " ".join([w[::-1] for w in sentence.split()])
print(rev)





