import random

predmeti = ['sword', 'bow', 'crossbow', 'staff off fire', 'staff of frost', 'staff of earth', 'staff of wind',
            'staff of lightning']
rooms = ['0', 'c', 'm', 't']


def razm():
    rooms = ['0', 'c', 'm', 't']
    n, m = random.randint(2, 5), random.randint(2, 5)
    print(n,m)
    polemoyo = []
    poleigrok = []
    prob = []
    for i in range(n):
        for j in range(m):
            prob.append(random.choice(rooms))
        polemoyo.append(prob)
        prob = []
    for i in range(n):
        for j in range(m):
            prob.append('*')
        poleigrok.append(prob)
        prob = []
    if 'k' not in polemoyo:
        x1, y1 = random.randint(0, n-1), random.randint(0, m-1)
        while x1 >= n or y1 >= m:
            x1, y1 = random.randint(0, n-1), random.randint(0, m-1)
        polemoyo[x1][y1] = 'k'
    if "p" not in polemoyo:
        x1, y1 = random.randint(0, n-1), random.randint(0, m-1)
        while x1 >= n or y1 >= m or polemoyo[x1][y1] == 'k':
            x1, y1 = random.randint(0, n-1), random.randint(0, m-1)
        polemoyo[x1][y1] = 'p'
    return poleigrok, polemoyo

def play(board, hp, items):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()
    print(f'{hp} хп, в инвенторе {items}')
    print('=====')
def issled(board, sec_board, x, y):
    board[y][x] = sec_board[y][x]
    return board

def igra():
    predmeti = ['sword', 'bow', 'crossbow', 'staff off fire', 'staff of frost', 'staff of earth', 'staff of wind',
                'staff of lightning']
    board, sec_board = razm()
    x, y = 0, 0
    hp = 100
    kluch = 0
    key__not_found = 1
    pobeda = 1
    items = ['', '', '']
    board = issled(board, sec_board, x, y)
    print("Ты находишься в глубоком подземелье! Попробуй найти выход и собрать хорошие вещи!")
    play(board, hp, items)
    while key__not_found:
        #rooms = ['0', 'c', 'm', 't'] + k + p
        if board[y][x] == '0':
            print("Эта комната пуста")
        elif board[y][x] == 'c':
            print("В этой комнате стоит сундук")
            predm = random.choice(predmeti)
            print("Вот твой инвентарь", items)
            print("Выбери в какой слот хочешь положить предмет(если в этом слоте уже что-то лежит, то этот предмет будет утерян)")
            slot = int(input())
            print('Вот что ты получил:', predm)
            while slot > 3 or slot < 1:
                print("Выбери корректный слот!")
                slot = int(input())
            items[slot - 1] = predm
        elif board[y][x] == 'm':
            print('Ты встречаешь в комнате монстра. Придется драться!')
            if items:
                print("Это было сложно, но ты справился, хоть монстр и нанес тебе небольшую травму.")
                hp -= 10
                if hp <= 0:
                    pobeda = 0
            else:
                print("Ты еле выжил")
                hp -= 70
                if hp <= 0:
                    pobeda = 0
        elif board[y][x] == 't':
            print("Ты попал в ловушку и получил урон.")
            hp -= 20
            if hp <= 0:
                pobeda = 0
        elif board[y][x] == 'k':
            print("Ты нашел ключ")
            kluch = 1
        elif board[y][x] == 'p':
            print("Поздравляю, ты нашел портал. Для его активации нужен ключ.")
            if kluch == 1:
                key__not_found = 0
                break
            else:
                print("Иди ищи ключ!!!")
        if hp > 0:
            print("Выбери направление движения:(wasd)")
            hod = input()
            flag = 1
            while flag:
                if hod == 'w':
                    if 0 <= y - 1 < len(board):
                        y = y - 1
                        flag = 0
                    else:
                        print("Ты уперся в стену.")
                elif hod == 'a':
                    if 0 <= x - 1 < len(board[0]):
                        x = x - 1
                        flag = 0
                    else:
                        print("Ты уперся в стену.")
                elif hod == 's':
                    if 0 <= y + 1 < len(board):
                        y = y + 1
                        flag = 0
                    else:
                        print("Ты уперся в стену.")
                elif hod == 'd':
                    if 0 <= x + 1 < len(board[0]):
                        x = x + 1
                        flag = 0
                    else:
                        print("Ты уперся в стену.")
                hod = input()
            issled(board, sec_board, x, y)
            play(board, hp, items)
            if pobeda == 0:
                flag = 0
        else:
            print("Несмотря на все твои старания, ты истек кровью")
            key__not_found = 0
    if pobeda:
        print("Ты выбрался из подземелья. Вот предметы которые ты собрал:", items)



igra()




