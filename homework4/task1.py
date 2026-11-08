n = int(input("Введите N: "))
zero_count = 0

for _ in range(n):
    num = int(input("Введите число: "))
    if num == 0:
        zero_count += 1

print(zero_count)