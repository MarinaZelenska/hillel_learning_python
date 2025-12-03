price = float(input("Введіть ціну: "))
discount = float(input("Введіть знижку (%): "))
final_price = price * (1 - discount / 100)
print("Ціна зі знижкою:", final_price)
