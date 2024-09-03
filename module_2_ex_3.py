



def print_row():
    my_row = [3, 13, 23, 33, 43]
    start_num = 3
    while start_num <= 43:
        print(start_num)
        start_num += 10


def check_password():
    int_pass = int(input('Input password, more than 8 characters: '))
    str_pass = str(int_pass)
    if len(str_pass) < 8:
        print('The password must contain at least 8 characters')
    else:
        print('The password is very good.')


def sale_car():
    params = input(f"Введите параметры автомобиля по шаблону \n 'LADA 2010г 205000км 450000руб'")
    info = params.split(' ')
    print(f"Продается автомобиль \n Марка : {info[0]} \n Год выпуска : {info[1]} \n Пробег : {info[2]} \n Цена : {info[3]}")



