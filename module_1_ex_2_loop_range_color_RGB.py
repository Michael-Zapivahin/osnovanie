import turtle

def  three_circles():
    t = turtle.Turtle()

    # Circle 1: Red, radius 50
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.begin_fill()
    t.color("red")
    t.circle(50)
    t.end_fill()

    # Circle 2: Green, radius 75
    t.penup()
    t.goto(100, 0)
    t.pendown()
    t.begin_fill()
    t.color("green")
    t.circle(75)
    t.end_fill()

    # Circle 3: Blue, radius 100
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.begin_fill()
    t.color("blue")
    t.circle(100)
    t.end_fill()

    # Finish
    turtle.done()


def three_figures():

    t = turtle.Turtle()

    t.penup()
    t.goto(-100, 250)
    t.pendown()
    t.begin_fill()
    t.color("#3498db")  # Синий цвет
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.end_fill()

    # Ромб: цвет #e74c3c (красный)
    t.left(30)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.begin_fill()
    t.color("#e74c3c")
    for _ in range(2):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.end_fill()

    # Трапеция: цвет #2ecc71 (зеленый)
    t.penup()
    t.left(60)
    t.goto(80, -200)
    t.pendown()
    t.begin_fill()
    t.color("#2ecc71")
    t.forward(200)
    t.right(120)
    t.forward(100)
    t.right(60)
    t.forward(150)
    t.right(60)
    t.forward(100)
    t.right(120)
    t.end_fill()

    turtle.done()


def green_christmas_tree():
    import turtle

    t = turtle.Turtle()
    t.speed(5)

    def draw_triangle(size):
        t.begin_fill()
        for _ in range(3):
            t.forward(size)
            t.left(120)
        t.end_fill()


    t.color("green")
    t.penup()
    t.goto(-75, -150)
    t.pendown()
    draw_triangle(150)

    t.penup()
    t.goto(-50, -50)
    t.pendown()
    draw_triangle(100)

    t.penup()
    t.goto(-25, 25)
    t.pendown()
    draw_triangle(50)

    t.hideturtle()
    turtle.done()


def three_squires():
    import turtle

    t = turtle.Turtle()
    t.speed(5)

    square_size = 30
    spacing = 30

    for i in range(3):
        t.penup()
        t.goto(-square_size // 2 + i * (square_size + spacing), 0)
        t.pendown()
        for _ in range(4):
            t.forward(square_size)
            t.right(90)

    t.hideturtle()
    turtle.done()

def seven_lines_cat():
    import turtle

    # Настройка turtle
    t = turtle.Turtle()
    t.speed(5)

    t.color("red")
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.forward(100)

    t.left(90)
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    t.forward(100)

    t.left(90)
    t.color("green")
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.forward(100)

    t.color("white")
    t.left(90)
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.forward(100)

    t.color("red")
    t.left(90)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.forward(100)

    t.color("green")
    t.left(90)
    t.penup()
    t.goto(50, 0)
    t.pendown()
    t.forward(100)

    # Линия 7 (в форме котенка )
    t.color("red")
    t.left(90)
    t.penup()
    t.goto(100, 0)
    t.pendown()
    t.left(180)
    t.circle(20)
    t.right(90)
    t.forward(40)
    t.left(135)
    t.forward(30)
    t.penup()

    t.hideturtle()
    turtle.done()