
number = input("Введите пятизначное целое число: ")

d1 = int(number[0]) 
d2 = int(number[1]) 
d3 = int(number[2]) 
d4 = int(number[3]) 
d5 = int(number[4])

result = (d4 ** d5 * d3) / (d1 - d2)

print(result)