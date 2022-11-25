# Задача 1________________________________________________________

import random
from statistics import mean

def student_number():
    student_number = random.randint(20, 30)
    return student_number

def group_number():
    group_number = random.randint(2,10)
    return group_number

def student_scores(a):
    student_scores = [random.randint(0,100) for i in range(a)]
    return student_scores

def list_group():
    list = []
    group_numb= group_number()
    for j in range(group_numb):
        student_numb = student_number()
        student_scor = student_scores(student_numb)
        list.append(student_scor)
    return list


def list_average(list):
    list_avg = []
    for i in list:
        avg = round(mean(i), 3)
        list_avg.append(avg)
    return list_avg

def print_list_group(list):
    for i in list:
        print(i)

def best_group(list):
    max_avg = max(list)
    max_avg_index = list.index(max_avg)
    print()
    print(f"Максимальный средний балл среди всех групп равен {max_avg},"+
    f" он принадлежит группе в строке {max_avg_index + 1}.")

a = list_group()
print_list_group(a)
b = list_average(a)
best_group(b)
