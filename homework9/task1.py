def get_factorial(n):
    if n in (0, 1):
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Введите натуральное число: "))

first_fact = get_factorial(num)

result_list = []
for i in range(first_fact, 0, -1):
    result_list.append(get_factorial(i))

print(result_list)