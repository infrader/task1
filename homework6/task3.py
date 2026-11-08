m = int(input("Грузоподъемность лодки (m): "))
n = int(input("Количество рыбаков (n): "))

weights = []
for _ in range(n):
    weights.append(int(input()))

weights.sort()

left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1 
        right -= 1 
    else:
        right -= 1 
        
    boats += 1

print(boats)