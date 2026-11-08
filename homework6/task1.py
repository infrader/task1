n = int(input("Введите N: "))
arr = []

for _ in range(n):
    arr.append(int(input()))

print(*arr[::-1])