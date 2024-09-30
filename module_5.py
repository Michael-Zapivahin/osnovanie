import tkinter as tk


def change_background_color():
    color = color_entry.get()
    try:
        canvas.config(bg=color)
    except tk.TclError:
        print("Ошибка: некорректный цвет. Попробуйте другой.")


root = tk.Tk()
root.title("Изменение цвета фона холста")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

color_entry = tk.Entry(root)
color_entry.insert(0, "white")
color_entry.pack()

change_color_button = tk.Button(root, text="Изменить цвет фона", command=change_background_color)
change_color_button.pack()


root.mainloop()
