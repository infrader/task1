import math

x = int(input("Введите X: "))
count = 0

for i in range(1, int(math.isqrt(x)) + 1):
    if x % i == 0:
        if i * i != x:
            count += 2
        else:
            count += 1

print(f"Количество натуральных делителей: {count}")