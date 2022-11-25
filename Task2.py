# Задача 2________________________________________________________

import random
from statistics import mean

def get_size():
    size = int(input("Введите размер куба: "))
    return size

def get_cube(size):
    cube = []
    for i in range(size):
        list_cube = [random.randint(1,9) for i in range(size)]
        cube.append(list_cube)   
    return cube

def print_cube(cube):
    for i in cube:
        print(i)

def get_amount(cube, size):
    amount = 0
    for i in range(size):
        for j in range(size):
            if cube[i] == cube[j]:
                amount += cube[i][j]
    return amount

def get_list_sum(cube):
    list_sum = []
    for i in cube:
        sum_list = sum(i)
        list_sum.append(sum_list)
        return list_sum

def get_index(list_sum, amount):
    index = []
    more_amount = []
    j = 0
    for i in list_sum: 
        if i > amount:
            index.append(j)
            more_amount.append(i)
        j += 1

    new_index =[]
    for i in index:
        i +=1
        new_index.append(i)
    return new_index

def list_change(new_index):
    list = ', '.join([str(x) for x in new_index])
    return list

def result(new_index, list):
    if not new_index:
        print("Нет строк сумма элементов, которых превосходит сумму главной диагонали матрицы.")
    else:
        print(f"Сумма элементов {list} строк/и превосходит сумму главной диагонали матрицы.")

a = get_size()
b = get_cube(a)
c = print_cube(b)
d = get_amount(b, a)
e = get_list_sum(b)
f = get_index(e, d)
g = list_change(f)
h = result(f, g)
