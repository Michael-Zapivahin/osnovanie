


def input_operation_number():
    valid_choices = ['1', '2', '3', '4', '5', '0']
    choice = None
    while choice not in valid_choices:
        choice = input("Выберите номер операции (1/2/3/4/5): ")
        if choice not in valid_choices:
            print("Неверный номер операции.")
        else:
            return int(choice)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Введите число.")


def read_file():
    try:
        with open("logs.txt", 'r') as file:
            print(file.read())
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def calc(choice: int):
    operation_text = ""
    if 1 <= choice <= 4:
        num_1 = get_number("Введите первое число: ")
        num_2 = get_number("Введите второе число: ")
    if choice == 1:
        result = num_1 + num_2
        operation_text = f"Результат: {num_1} + {num_2} = {result}"
    elif choice == 2:
        result = num_1 - num_2
        operation_text = f"Результат: {num_1} - {num_2} = {result}"
    elif choice == 3:
        result = num_1 * num_2
        operation_text = f"Результат: {num_1} * {num_2} = {result}"
    elif choice == 4:
        if num_2 == 0:
            print("Ошибка: деление на ноль")
        else:
            result = num_1 / num_2
            operation_text = f"Результат: {num_1} / {num_2} = {result:.2f}"
    elif choice == 5:
        read_file()
    else:
        operation_text = "Неверный выбор операции."

    print(operation_text)

    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write(f'Операция: {operation_text}.\n')


def main():
    valid_operations = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
        "5": "Прочитать лог",
        "0": "Завершить",
    }
    print("Список доступных операций-")
    for key, value in valid_operations.items():
        print(key, value)
    choice = ""
    while True:
        choice = input_operation_number()
        if choice == 0:
            return
        calc(choice)


if __name__ == "__main__":
    main()
