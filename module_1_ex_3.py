

def draw_squares():
    import turtle

    t = turtle.Turtle()
    t.ht()
    t.pensize(5)
    t.speed(0)

    for r in range(40, 0, -10):
        for i in range(6):
            t.color(255, 165, r * 6)
            t.fillcolor(162, r * 6, 255)
            t.begin_fill()
            # start square
            for _ in range(4):
                t.forward(r * 2)
                t.right(90)
            # end square
            t.end_fill()
            t.rt(60)


def draw_trapezoid():
    import turtle

    t = turtle.Turtle()
    t.ht()  # Скрываем черепашку
    t.pensize(5)  # Устанавливаем толщину линии
    t.speed(0)  # Устанавливаем максимальную скорость рисования
    x_pos, y_pos = 0, 0
    # Рисуем узор из трапеций, которые соприкасаются боками
    for r in range(40, 0, -10):
        for i in range(6):
            t.color(255, 165, r * 6)  # Устанавливаем цвет линии
            t.fillcolor(162, r * 6, 255)  # Устанавливаем цвет заливки
            t.begin_fill()

            base = r * 2  # Нижнее основание трапеции
            height = 20  # Высота трапеции
            top = base - height  # Верхнее основание трапеции

            # Рисуем трапецию
            t.forward(base)  # Нижняя сторона
            t.rt(120)
            t.forward(height)  # Левая наклонная сторона
            t.rt(60)
            t.forward(top)  # Верхняя сторона
            t.rt(60)
            t.forward(height)  # Правая наклонная сторона
            t.rt(120)

            t.end_fill()

            t.penup()
            t.forward(base)  # Перемещение черепашки к началу следующей трапеции
            t.pendown()
            t.rt(60)

        t.penup()
        x_pos, y_pos = x_pos + height / 2, y_pos - (height - 3)
        t.goto(x_pos, y_pos)
        t.pendown()

