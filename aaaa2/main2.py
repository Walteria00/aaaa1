# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
from copy import deepcopy
from sys import int_info

numbers=[1,2,3,4,5,6,7,8,9]
lista=deepcopy(numbers)
print(id(lista))
print(id(numbers))

lista.append(323)
print(lista)
print(numbers)

print(id(lista.append(323)))
print(id(numbers))

porownanie=lista==numbers
print(porownanie)