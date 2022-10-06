
#1- Определить, присутствует ли в заданном списке строк, некоторое число

one_list = ['dt34fd', '456fgsrt', 'hj46yjj67', '99jdyj']
namber = '6'
sym_contains = False
for element in one_list:
    if namber in element:
        sym_contains = True
        break
print("Символ содержиться в списке: ", sym_contains)
result = list(filter(lambda element: namber in element, one_list))
print("Строки, где содержится число: ", result)


#2 - Найти сумму чисел списка стоящих на нечетной позиции


from functools import reduce
some_list = [1,567,-46,578,568,-365]
sum_el1 = sum(list(filter(lambda el: some_list.index(el) % 2 != 0, some_list)))
sum_el2 = reduce(lambda el1, el2: el1+el2, list(filter(lambda el: some_list.index(el) % 2 != 0, some_list)))
print(sum_el1, sum_el2)


#3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

point1 = '65 69'
point2 = '4 6'
pos1 = list(map(lambda p: float(p), point1.split(' ')))
pos2 = list(map(lambda p: float(p), point2.split(' ')))
distance = ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**0.5
print(distance)



#4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

some_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
def search_second_index(l:list, s:str):
    index = -1
    num_found_sym = 0
    for i in range(len(l)):
        if s == l[i]:
            num_found_sym += 1
            if num_found_sym == 2:
                index = i
                break
    return index
print(search_second_index(some_list, 'qwe'))


#5 - Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math
some_list = [1,567,-46,578,54,568,-365]
part_len = math.ceil(len(some_list)/2)
new_list = list(map(lambda i: some_list[i] * some_list[len(some_list) - i - 1], range(part_len)))
print(new_list)



#6 - Сформировать список из N членов последовательности.


N = int(input("Enter N: "))
print(list(map(lambda x: (-3)**x, range(N))))