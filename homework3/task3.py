x = int(input("Минимальная сумма инвестиций (X): "))
a = int(input("Сумма Майкла (A): "))
b = int(input("Сумма Ивана (B): "))

if a >= x and b >= x:
    print(2)
elif a >= x:
    print("Mike")
elif b >= x:
    print("Ivan")
elif a + b >= x:
    print(1)
else:
    print(0)