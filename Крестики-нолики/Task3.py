# Создайте программу для игры в ""Крестики-нолики"".
from emoji import *
def pole_print(list): # Вывод поля на экран
    print('  0','  ', '1', '  ', '2')    
    for i in range(len(list)):
        for j in range(len(list[i])):
            print (list[i][j], end='')
        print(i)
def winner_check_rows (list, status): # Проверка условия победы по строкам и диагоналям
    for i in range(len(list)):
        count1 = 0
        count2 = 0
        for j in range(len(list[i])):
            if list[i][j] == '  X  ': 
                count1 += 1
            if list[i][j] == '  0  ':
                count2 += 1
            if list[0][0] == list[1][1] == list[2][2] == '  X  ' \
                or list[2][0] == list[1][1] == list[0][2] == '  X  ':
                count1 = 3
            if list[0][0] == list[1][1] == list[2][2] == '  0  ' \
                or list[2][0] == list[1][1] == list[0][2] == '  0  ':
                count2 = 3
        if count1 == 3:
            status = 1
            break
        if count2 == 3:
            status = 2
            break
        else: status = 0
    return(status)
def winner_check_colms(list,status): # Проверка условия победы по колонкам
    for i in range(len(list)):
        count1 = 0
        count2 = 0
        for j in range(len(list[i])):
            if list[j][i] == '  X  ': 
                count1 += 1
            if list[j][i] == '  0  ':
                count2 += 1
        if count1 == 3:
            status = 1
            break
        if count2 == 3:
            status = 2
            break
        else: status = 0            
    return(status) 
def turn(list, n): # Проверка на правильность ввода пользователем
    while True:
        i = input('Введите номер строки: ')
        j = input('Введите номер столбца: ')
        try:
            i = int(i)
            j = int(j)
            if 0<=i<=2 and 0<=j<=2 and list[i][j] == ' | | ':
                if n == 1:
                    list[i][j] = '  X  '
                else:
                    list[i][j] = '  0  '
                break
            else:
                print('Недопустимое значение индекса или поле занято!')
        except:
            print('Нужно вводить числа!')
    return list[i][j]
def no_winner(list): # Проверка на ничью
    check = []
    for a in list:
        check.extend(a)
    if check.count(' | | ') == 0:
        n = 3
    else:
        n = 0
    return(n)

print('Привет!  Добро пожаловать в игру "крестики-нолики"')
name_one = (input('Введите имя первого игрока: '))
name_two = (input('Введите имя второго игрока: '))
pole =[[' | | ']*3 for i in range (3)]
pole_print(pole)

print('Перед Вами поле! Сверху номера столбцов, справа номера строк')
Flag = 0

for _ in range (5):
    print(f'{name_one}', 'Ваш ход, вы ставите крестики')
    turn(pole,1)
    pole_print(pole)
    winner = winner_check_rows(pole, Flag)
    if winner == 1:
        break
    winner = winner_check_colms(pole, Flag)
    if winner == 1:
        break
    winner = no_winner(pole)
    if winner == 3:
        break
    print(f'{name_two}', 'Ваш ход, вы ставите нолики')
    turn(pole,2)
    pole_print(pole) 
    winner = winner_check_rows(pole, Flag)
    if winner == 2:
        break
    winner = winner_check_colms(pole, Flag)
    if winner == 2:
        break

if winner == 1:
    print(emojize(f'{name_one} Вы выиграли! :thumbs_up:'))
if winner == 2:
    print(emojize(f'{name_two} Вы выиграли!:thumbs_up:'))
if winner == 3:
    print('У Вас ничья! Попробуйте снова')
