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
        f_vars = expr.free_symbols
        f = sympy.lambdify('x', expr)

        # Если в выражении нет переменной x, сообщаем об ошибке
        if sympy.core.symbol.Symbol('x') not in f_vars:
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


def draw_grafics_2tab():
    if t_left_limit.get() == '' or t_right_limit.get() == '' or x_formula_input.get() == '' or y_formula_input.get() == '':
        messagebox.showinfo("ОШИБКА", "Заполните все поля")
    else:
        # Принимаем строку с поля ввода
        x_expr_str = str(x_formula_input.get())
        y_expr_str = str(y_formula_input.get())
        # Преобразуем строку в символьное выражение
        x_expr = sympy.sympify(x_expr_str)
        y_expr = sympy.sympify(y_expr_str)
        # Получаем список переменных в выражении
        vars_x = x_expr.free_symbols
        vars_y = y_expr.free_symbols
        f_x = sympy.lambdify('t', x_expr)
        f_y = sympy.lambdify('t', y_expr)
        # Если в выражении нет переменной x, сообщаем об ошибке
        if sympy.core.symbol.Symbol('t') not in vars_x and sympy.core.symbol.Symbol('t') not in vars_y:
            messagebox.showinfo("ОШИБКА", "В функции нет переменной t")
        else:
            t_vals = np.linspace(float(t_left_limit.get()), float(t_right_limit.get()), 100000)
            x_vals = f_x(t_vals)
            y_vals = f_y(x_vals)

            # Отображаем график
            plt.plot(x_vals, y_vals)
            plt.xlabel('X')
            plt.ylabel('Y')
            # plt.title()
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
notebook.add(tab1, text='y = f(x)')

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
notebook.add(tab2, text='x = f(t), y = g(t)')

# Добавление элементов управления на вторую вкладку

# Ввод уравнения x(t)
x_formula_lb = tk.Label(tab2, text="Введите уравнение: x(t) =")
x_formula_lb.grid(column=0, row=0, padx=5, pady=5, sticky='w')

x_formula_input = tk.Entry(tab2)
x_formula_input.grid(column=1, row=0, padx=5, pady=5)

# Ввод уравнения y(t)
y_formula_lb = tk.Label(tab2, text="Введите уравнение: y(t) =")
y_formula_lb.grid(column=0, row=1, padx=5, pady=5, sticky='w')

y_formula_input = tk.Entry(tab2)
y_formula_input.grid(column=1, row=1, padx=5, pady=5)

# Ввод левой границы
t_left_limit_lb = tk.Label(tab2, text="Введите левую границу t:")
t_left_limit_lb.grid(column=0, row=2, padx=5, pady=5, sticky='w')

t_left_limit = tk.Entry(tab2)
t_left_limit.grid(column=1, row=2, padx=5, pady=5)

# Ввод правой границы
t_right_limit_lb = tk.Label(tab2, text="Введите правую границу t:")
t_right_limit_lb.grid(column=0, row=3, padx=5, pady=5, sticky='w')

t_right_limit = tk.Entry(tab2)
t_right_limit.grid(column=1, row=3, padx=5, pady=5)

# Кнопка вызова функции
t_cal_btn = tk.Button(tab2, text='Построить график', command=draw_grafics_2tab)
t_cal_btn.grid(column=1, row=4, padx=5, pady=5)

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
