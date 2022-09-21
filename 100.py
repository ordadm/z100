# Есть 100 заключенных, с ними решили провести следующий эксперимент.
# Их всех амнистируют, если каждый выполнит такое задание:
# есть комната, в комната 100 коробочек, в каждой коробочке номер заключенного.
# заключенный входит в комнату, открывает коробочку, смотрит какой там номер - если там его номер,
# он выходит в комнату кандидатов на освобождение. Если там не его номер, он повторяет попытку.
# Но проверить он может не более 50 коробочек. Если после 50 попыток, он не находит свой номер, эксперимент прекращается
# и всех, 100, заключенных казнят.
# Наша задача экспериментальным путём выяснить с какой вероятностью все заключенные выживут
# Конечно все зависит от алгоритма по которому заключенные будет искать свой номер
# Подробнее про задачу и самый оптимальный алгоритм  можно посмотреть на ютубе в ролике https://www.youtube.com/watch?v=wWQ9YdreY9c
# Описаный в ролике алгоритм предполагает вероятность порядка 30%. Причем внезависимости от количества заключенных и коробок
# Хотя, на первый взгляд вероятность для одного заключенного 50%, а учитывая что их сто, вероятность что найдут все это 0.5 в 100 степени
# В общем ничтоножно малая вероятность.
# Ну что ж, начнем экспериментировать!

import random

# определяем количество заключенных
# qtyprisoner:int=int(input("Введите количество заключенных: "))
qtyprisoner: int = 100
qtymissions: int = 100000
qtychance: int = 50


# #определяем количество экспериментов
# qtyexperiment:int=int(input("Введите количество экспериментов (не менее 100): "))

# создание комнаты
def makeroom() -> dict:
    # room = list(range(1, qtyprisoner + 1))
    # random.shuffle(room)
    room: set = set()
    while len(room) < qtyprisoner:
        rand = str(random.randint(1, qtyprisoner))
        room.add(rand)
    lroom: list = list(room)
    random.shuffle(lroom)
    droom = dict()
    for i in range(0, qtyprisoner):
        droom.setdefault(i + 1, int(lroom[i]))
    return droom


def openfirstbox(room, number_prisoner):
    secondbox = room.get(number_prisoner)
    return secondbox


def opennextbox(room, nextbox):
    box = room.get(nextbox)
    return box


def wayprisoner(room, prisoner):
    nextbox = openfirstbox(aroom, prisoner)
    if nextbox == prisoner:
        chance = 1
        print('заключенный №', prisoner, 'c ', chance, ' попытки')
        return True
    else:
        chance = 2
        nextbox = opennextbox(room, nextbox)
        while chance <= qtychance:

            if nextbox == prisoner:
                print('заключенный №', prisoner, 'c ', chance, ' попытки')
                return True
            chance += 1
            nextbox = opennextbox(room, nextbox)
        return False

#aroom={1: 9, 2: 6, 3: 7, 4: 4, 5: 8, 6: 3, 7: 5, 8: 10, 9: 1, 10: 2}



# for pris in range(1,qtyprisoner+1):
#
#     print(wayprisoner(aroom,pris))

# for pris in range(1, qtyprisoner + 1):
#     print(f'Заключенный {pris} Шанс1')
#     nextbox = openfirstbox(aroom, pris)
#     print(f'{pris} -> {nextbox}')
#     chance = 2
#     for c in range(chance, qtychance+1):
#         print(f'Заключенный {pris} Шанс,{c}')
#         print(f'{nextbox} -> {opennextbox(aroom, nextbox)}')
#         nextbox = opennextbox(aroom, nextbox)



def mission(room):
    for np in range(0, qtyprisoner):  # выбираем заключенных по одному
        number_prisoner = np + 1
        if wayprisoner(aroom, number_prisoner) == False:
            return False

    return True

positiv = 0

for stat in range(1, qtymissions+1):
    aroom = makeroom()
    print(f'миссия №, {stat}, стартовала')
    print(aroom)

    if mission(aroom) == True:
        print(f'миссия№ {stat} успешна')
        positiv += 1
    else:
        print ('миссия №',stat,'провалена')
print(f'Пройденых миссий {positiv}')
