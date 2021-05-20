from django.test import TestCase


# a = range(0, 3)
# for i in a:
#     print(i)
#
#
# def generator():
#     list = range(0, 3)


# class A:
#     def __init__(self, question1, question2):
#         self.question1 = question1
#         self.question2 = question2
#
#     question1 = input('Введите первое число: ')
#     question2 = input('Введите второе число: ')
#     my_list = range(int(question1), int(question2))
#     for i in my_list:
#         print(i)
#
#
# Vlad = A


# class B:
#     def __init__(self):
#         self.start = int(input('Введите Start: '))
#         self.end = int(input('Введите Stop: '))
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.end >= self.start:
#             self.start += 1
#             return self.start - 1
#         else:
#             raise StopIteration
#
#
# a = B()
#
# for i in a:
#     print(i)


# s =[i for i in range(1,10,2)]
# print(s)

# def get_student_names(students):
#     a=[]
#     a.append(students['student1'])
#     a.append(students['student2'])
#     a.append(students['student3'])
#     a.sort()
#     return print(a)


# get_student_names({'student1': 'Артём', 'student2': 'Максим', 'student3': 'Иван'})


def society_name(friends):
    # a=''
    # for i in friends:
    #     a=a+i[0:1].upper()
    # print(a)
    return print(sorted(''.join([i[0:1].upper() for i in friends])))

society_name(['Артём', 'Екатерина', 'Максим'])
