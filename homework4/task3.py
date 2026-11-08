a = int(input("Введите A: "))
b = int(input("Введите B: "))

if a % 2 != 0:
    a += 1

print(*range(a, b + 1, 2))