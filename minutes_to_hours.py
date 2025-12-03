minutes = int(input("Введіть кількість хвилин: "))

hours, mins = divmod(minutes, 60)

print(f"{hours} години {mins} хвилин")
