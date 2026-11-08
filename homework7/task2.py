list1 = set(map(int, input().split()))
list2 = set(map(int, input().split()))

common_elements = list1 & list2
print(len(common_elements))