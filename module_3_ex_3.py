import random


first_words = ['блистательно', 'неотразимо', 'восхитительно', 'очаровательно', 'изумительно']
second_words = ['прекрасна', 'мила', 'красива', 'прекрасна', 'чудесна']


def generate_compliment():
    first = random.choice(first_words)
    second = random.choice(second_words)
    return f"Ты {first} {second}!"


def task_1():
    for _ in range(5):
        print(generate_compliment())


def task_2():
    s = [x for x in range(10, 4, -1)]
    print(s)


def task_3():
    words = ["море", "солнце", "майка", "отпуск"]
    e_words = [i for i in words if i.endswith('е')]
    print(e_words)

