n = int(input("Введите N: "))
arr = list(map(int, input().split()))

shifted_arr = arr[-1:] + arr[:-1]

print(*shifted_arr)