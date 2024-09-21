import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        messagebox.showinfo("Результат сложения", f"Сумма: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа.")


def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        result = num1 * num2 * num3
        messagebox.showinfo("Результат умножения", f"Произведение: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа.")


root = tk.Tk()
root.title("Калькулятор")


ttk.Label(root, text="Число 1:").pack(pady=5)
entry1 = ttk.Entry(root)
entry1.pack(pady=5)

ttk.Label(root, text="Число 2:").pack(pady=5)
entry2 = ttk.Entry(root)
entry2.pack(pady=5)

ttk.Label(root, text="Число 3:").pack(pady=5)
entry3 = ttk.Entry(root)
entry3.pack(pady=5)


add_button = ttk.Button(root, text="Сложить 2 числа", command=add_numbers)
add_button.pack(pady=10)

multiply_button = ttk.Button(root, text="Умножить 3 числа", command=multiply_numbers)
multiply_button.pack(pady=10)


root.mainloop()
