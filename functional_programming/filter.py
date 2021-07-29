'''возвращает значение, для которого выражение истинно'''

numbers = [10, 4, 2, -1, 6]
l1 = list(filter(lambda x: x < 5, numbers))    # В результат попадают только те элементы x, для которых x < 5 истинно
print(l1)

# То же самое с помощью списковых выражений:

numbers = [10, 4, 2, -1, 6]
l2 = [x for x in numbers if x < 5]
print(l2)