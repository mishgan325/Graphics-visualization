"""
from tkinter import *
from tkinter import messagebox
import sympy
import matplotlib.pyplot as plt
import numpy as np


def draw_grafics():
    if left_limit.get() == '' or right_limit.get() == '' or formula_input.get() == '':
        messagebox.showinfo("ОШИБКА", "Заполните все поля")
    else:
        # Принимаем строку с поля ввода
        expr_str = str(formula_input.get())
        # Преобразуем строку в символьное выражение
        expr = sympy.sympify(expr_str)
        # Получаем список переменных в выражении
        vars = expr.free_symbols
        f = sympy.lambdify('x', expr)

        # Если в выражении нет переменной x, сообщаем об ошибке
        if sympy.core.symbol.Symbol('x') not in vars:
            messagebox.showinfo("ОШИБКА", "В функции нет перемнной x")
        else:
            x_vals = np.linspace(float(left_limit.get()), float(right_limit.get()), 100000)
            y_vals = f(x_vals)

            # Отображаем график
            plt.plot(x_vals, y_vals)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title(expr_str)
            #plt.title(r'$y = \sqrt{x}$')
            print(fr'${sympy.latex(expr_str)}$')
            plt.grid()
            plt.show()


window = Tk()
window.title('Построение графиков')
window.geometry('400x300')

# заготовка стандартных размеров
frame = Frame(window, padx=10, pady=10)
frame.pack(expand=True)

formula_lb = Label(frame, text="Введите уравнение: y =")
formula_lb.grid(row=3, column=1)

formula_input = Entry(frame)
formula_input.grid(row=3, column=2, pady=5)


left_limit_lb = Label(frame, text="Введите левую границу x:")
left_limit_lb.grid(row=4, column=1)

left_limit = Entry(frame)
left_limit.grid(row=4, column=2, pady=5)


right_limit_lb = Label(frame, text="Введите правую границу x:")
right_limit_lb.grid(row=5, column=1)

right_limit = Entry(frame)
right_limit.grid(row=5, column=2, pady=5)

cal_btn = Button(frame, text='Построить график', command=draw_grafics)
cal_btn.grid(row=7, column=2)

window.mainloop()
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sympy
import matplotlib.pyplot as plt
import numpy as np

def draw_grafics():
    if left_limit.get() == '' or right_limit.get() == '' or formula_input.get() == '':
        messagebox.showinfo("ОШИБКА", "Заполните все поля")
    else:
        # Принимаем строку с поля ввода
        expr_str = str(formula_input.get())
        # Преобразуем строку в символьное выражение
        expr = sympy.sympify(expr_str)
        # Получаем список переменных в выражении
        vars = expr.free_symbols
        f = sympy.lambdify('x', expr)

        # Если в выражении нет переменной x, сообщаем об ошибке
        if sympy.core.symbol.Symbol('x') not in vars:
            messagebox.showinfo("ОШИБКА", "В функции нет перемнной x")
        else:
            x_vals = np.linspace(float(left_limit.get()), float(right_limit.get()), 100000)
            y_vals = f(x_vals)

            # Отображаем график
            plt.plot(x_vals, y_vals)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title(expr_str)
            # plt.title(r'$y = \sqrt{x}$')
            # print(fr'${sympy.latex(expr_str)}$')
            plt.grid()
            plt.show()

# Создание корневого окна
window = tk.Tk()
window.title('Построение графиков')
# window.geometry('400x300')

# Создание виджета Notebook
notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

# Создание первой вкладки
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Вкладка 1')

# Добавление элементов управления на первую вкладку

# Ввод уравнения
formula_lb = tk.Label(tab1, text="Введите уравнение: y =")
formula_lb.grid(column=0, row=0, padx=5, pady=5, sticky='w')

formula_input = tk.Entry(tab1)
formula_input.grid(column=1, row=0, padx=5, pady=5)

# Ввод левой границы
left_limit_lb = tk.Label(tab1, text="Введите левую границу x:")
left_limit_lb.grid(column=0, row=1, padx=5, pady=5, sticky='w')

left_limit = tk.Entry(tab1)
left_limit.grid(column=1, row=1, padx=5, pady=5)

# Ввод правой границы
right_limit_lb = tk.Label(tab1, text="Введите правую границу x:")
right_limit_lb.grid(column=0, row=2, padx=5, pady=5, sticky='w')

right_limit = tk.Entry(tab1)
right_limit.grid(column=1, row=2, padx=5, pady=5)

# Кнопка вызова функции
cal_btn = tk.Button(tab1, text='Построить график', command=draw_grafics)
cal_btn.grid(column=1, row=3, padx=5, pady=5)



# Создание второй вкладки
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Вкладка 2')

# Добавление элементов управления на вторую вкладку
label2 = tk.Label(tab2, text='Это элемент управления на второй вкладке')
label2.pack()

# Запуск основного цикла
window.mainloop()











# try:
#     # Принимаем строку с поля ввода
#     expr_str = str(formula_input.get())
#     # Преобразуем строку в символьное выражение
#     expr = sympy.sympify(expr_str)
#     # Получаем список переменных в выражении
#     vars = expr.free_symbols
#     f = sympy.lambdify('x', expr)
# except KeyError:
#     print("Деление на ноль!")
#     res = messagebox.askquestion('ОШИБКА!', 'Деление на ноль!')
#     expr_str = str(formula_input.get())
#     # Преобразуем строку в символьное выражение
#     expr = sympy.sympify(expr_str)
#     # Получаем список переменных в выражении
#     vars = expr.free_symbols
#     f = sympy.lambdify('x', expr)