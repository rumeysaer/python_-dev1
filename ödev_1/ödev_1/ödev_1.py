list1 = [1,3,5,7,9]
list2 = [2,4,6,8]
list1.extend(list2)
list1.sort()
print(list1)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [i*2 for i in list1]
print(numbers)
[2, 4, 6, 8, 10, 12, 14, 16, 18]
